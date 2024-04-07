### Program note:
### List of players is shuffled not list of party membership
### I use "party membership"/membership and "roles" interchangably in my comments

### Game note:      This should be announced at the beginnging of the game
### Link to rules: https://www.secrethitler.com/assets/Secret_Hitler_Rules.pdf
### Players are to be careful in typing and pressing Enter, it may cause program to crash
### The computer should be facing away from the rest of the players
### There should never be 2 players at the computer simultaneously
### Read instructions on screen CAREFULLY, any doubts ask
### Don't cheat by scrolling upwards
### Election of Chancellor and movement of President is not managed by the program, it is simple enough
### Player should not forget their role it is tedious though not impossible to check
### President and Chancellor choose a card to DISCARD not to keep and they must be careful, no taking back their selection

import random
game_state = False  ### Used to end the game when a Party has won
players = []        ### List of players
order_players = []  ### Used in party_membership_view() to show roles without revealing anything
party_mem = []      ### Roles of players ie Party Memebership
deck = []           ### Deck of Policies
discard = []        ### Discard pile
lib_board = 0       ### Number of Liberal Policies placed
fac_board = 0       ### Number of Facists Policies placed

def addplayer():
    name = input("Enter name\n").lower()
    players.append(name)
    order_players.append(name)

### Function should have been called setup but I'm too scared of errors to change it
### Add players to the game ("players" list)
### Adds number of roles of each party depending on how many players there are
### "Assigns" roles to each player (Actually the postion of the players in the list are lined up to the position of the membership roles in the other list)
### Shuffles list of players

def game_start(game_state, lib_board, fac_board):
    game_state = True
    num_players = input("How many players in the game?\n")
    if num_players.isnumeric() == True:         ### Error catching
        num_players = int(num_players)
    elif num_players == "":
        print("Incorrect input.Try again\n")
        game_start(game_state, lib_board, fac_board)
    else:
        print("Incorrect input.Try again\n")
        game_start(game_state, lib_board, fac_board)

    if num_players < 5:                             ###Lower band
        print("Too few players\n")
        game_start(game_state, lib_board, fac_board)
    elif num_players > 10:                          ###Upper band
        print("Too many players\n")
        game_start(game_state, lib_board, fac_board)

    ### Calculates correct number of Liberal and Facist players, trust me it works
    if num_players % 2 == 0:
        numliberals = num_players - (num_players/2 + 1)
        numfacists = (num_players-4)/2
    else:
        numliberals = (num_players+1) - ((num_players+1)/2 + 1)
        numfacists = ((num_players-1)-4)/2

    ### Assign roles - Adds correct number of Facists and Liberals, as well as Secret Hitler to the list party_mem
    for i in range(numfacists):
        party_mem.append("Facist")
    party_mem.append("Secret Hitler")
    for i in range(numliberals):
        party_mem.append("Liberal")
    ### Shuffles the players, list with roles (party_mem) isn't shuffled
    for i in range(num_players):
        addplayer()
    random.shuffle(players)
    random.shuffle(players) ### To make sure it's Really shuffled
    random.shuffle(players)
    print(players)

        ### Create a deck
    for i in range(8):
        deck.append("Liberal")
    for i in range(11):
        deck.append("Facist")
    random.shuffle(deck)

    party_membership_view() ### To show each player their role

def party_membership_view():
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    next_ = input("Press Enter to continue.\n") ### Access to secret menu
    menu(next_)
    for person in order_players:
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        pos = players.index(person)
        print(person)
        next_ = input("Press Enter to show role.") ### Gives spacing so player sees their own and not the next's
        print("\nYou are",party_mem[pos])
        next_ = input("Press Enter to continue.")  ### Gives spacing so player sees their own and not the next's
    rounds(lib_board, fac_board)

def rounds(lib_board, fac_board):
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    next_ = input("Press Enter to continue.\n") ### Access to secret menu
    menu(next_)
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    ### President selection of cards
    draw = input("Draw cards(Press Enter)")
    print(deck[:3])
    selection = input("Discard a card(1, 2 or 3)\n")
    if selection.isnumeric() == True:    ### Error catching
        selection = int(selection)
        if selection < 1 or selection > 3:
            print("Invalid selection. Try again\n")
            rounds(lib_board, fac_board)
        selection -=1 ### Does this so it can be used as the index to move the item
        discard.append(deck[selection])
        deck.pop(selection)
        ### So Chancellor doesn't see President's selection
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        chancellor_selection(lib_board, fac_board)
    else:
        rounds(lib_board, fac_board)

    ### Chancellor selection of cards
def chancellor_selection(lib_board, fac_board):
    print(deck[:2])
    selection = input("Discard a card(1 or 2)\n")
    if selection.isnumeric() == True:   ### Error catching
        selection = int(selection)
        if selection < 1 or selection > 2:
            print("Invalid selection. Try again\n")
            rounds(lib_board, fac_board)
        selection -=1 ### Does this so it can be used as the index to move the item
        discard.append(deck[selection])
        deck.pop(selection)
        if deck[0] == "Liberal":
            lib_board += 1
            if lib_board == 5:
                print("End of game Liberals won")
                game_state = False
            else:
                rounds(lib_board, fac_board)
        else:
            fac_board += 1
            if fac_board == 6:
                print("End of game Facists won")
                game_state = False
            else:
                president_powers(fac_board)
    else:
        chancellor_selection(lib_board, fac_board)

def president_powers(fac_board):
    print("President's powers. Chancellor go away.\n")
    if fac_board == 1 or fac_board == 2:
        player_choice = input("Enter a player to investigate.\n").lower()
        if player_choice in players:    ### Check input is an actual player
            pos = players.index(player_choice)
            if party_mem[pos] == 'Secret Hitler':
                print('Facist')         ### To not reveal Hitler's identity
            else:
                print(party_mem[pos])
        else:
            print("Player is dead or not in player list. Try again.\n")
            president_powers(fac_board)

    elif fac_board == 3:
        print("Choose the next President.\n")

    elif fac_board == 4 or fac_board == 5:
        player_choice = input("Choose a player to kill.\n").lower()
        if player_choice in players:
            pos = players.index(player_choice)
            if party_mem[pos] == "Secret Hitler":
                print("End of game Liberals won")
                game_state = False  ### End of game
            else:
                players.pop(pos)    ### Removes player from list
                party_mem.pop(pos)  ### Removes party membership from list
        else:
            president_powers()

    next_ = input("Press Enter for next round\n")
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    rounds(lib_board, fac_board)

def menu(next_):        ### Access to secret menu
    if next_ == "2002": ### Password to access menu
        choice = input("Menu:Change name of player(1)\nCheck role of a player(2)\nList players(3)\nList roles(4)\nExit(5)")
        if choice == "1":
            ### Removes old name and inserts new name
            current_name = input("Enter name of player whose name is to be changed.").lower()
            if current_name in players:
                pos = players.index(current_name)
                players.pop(pos)
                new_name = input("Enter new name of player.").lower()
                players.insert(pos,new_name)
            else:
                print("Invalid input")
                next_ = "2002" ### Return to top
                menu(next_)
        elif choice == "2":
            ### In case players forget
            name = input("Enter name of player whose role you want to check.")
            if name in players:
                pos = players.index(name)
                print(party_mem[pos])
            else:
                print("Invalid input.\n")
                next_ = "2002" ### Return to top
                menu(next_)
        elif choice == "3":
            ### To see players left
            print(players)
        elif choice == "4":
            ### To see how many roles are left
            print(party_mem)
        elif choice == "5":
            return
        else:
            print("Invalid input.\n")
            next_ = "2002" ### Return to top of function
            menu(next_)
    else:
        return ### Back to function which called this one

game_start(game_state,lib_board, fac_board)

### Junk, do what you will with it

#     assigned = []
#     index_pos = 0
#     for person in players:
#         assigned.append(person)
#         assigned.append(party_mem[index_pos])
#         index_pos += 1#
#     print(assigned)

# def change_num_players():
#     change = input("Change in number of players?(y/n)\n").lower()
#     if change == "y":
#         newnumplayers = int(input("Enter new number of players\n"))
#         numplayers = newnumplayers
#         setup()
#     elif change == "n":
#         main_menu()
#     else:
#         pass



