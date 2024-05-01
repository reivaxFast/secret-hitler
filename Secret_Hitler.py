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

import random, os

class game: ### Number of Facists Policies placed
    def __init__(self) -> None:
        self.output = open('output.txt', 'w')
        self.game_state = False  ### Used to end the game when a Party has won
        self.players = []        ### List of players
        self.order_players = []  ### Used in party_membership_view() to show roles without revealing anything
        self.party_mem = []      ### Roles of players ie Party Memebership
        self.deck = []           ### Deck of Policies
        self.discard = []        ### Discard pile
        self.lib_board = 0       ### Number of Liberal Policies placed
        self.fac_board = 0
        self.num_players = 0
        #self.game_start()
    
    def addplayer(self):
        name = input("Enter name\n").lower()
        self.players.append(name)
        self.order_players.append(name)
        

    ### Function should have been called setup but I'm too scared of errors to change it
    ### Add players to the game ("players" list)
    ### Adds number of roles of each party depending on how many players there are
    ### "Assigns" roles to each player (Actually the postion of the players in the list are lined up to the position of the membership roles in the other list)
    ### Shuffles list of players

    def game_start(self):
        self.game_state = True
        self.num_players = input("How many players in the game?\n")
        if self.num_players.isnumeric() == True:         ### Error catching
            self.num_players = int(self.num_players)
        else:
            print("Incorrect input.Try again\n")
            self.game_start()

        if self.num_players < 5:                             ###Lower band
            print("Too few players\n")
            self.game_start()
        elif self.num_players > 10:                          ###Upper band
            print("Too many players\n")
            self.game_start()

        ### Calculates correct number of Liberal and Facist players, trust me it works
        if self.num_players % 2 == 0:
            self.numliberals = self.num_players - (self.num_players/2 + 1)
            self.numfacists = (self.num_players-4)/2
        else:
            self.numfacists = (self.num_players-3)/2
            self.numliberals = self.num_players - (self.numfacists + 1)

        ### Assign roles - Adds correct number of Facists and Liberals, as well as Secret Hitler to the list party_mem
        self.numfacists = int(self.numfacists)
        self.numliberals = int(self.numliberals)
        for i in range(self.numfacists):
            self.party_mem.append("Facist")
        self.party_mem.append("Secret Hitler")
        for i in range(self.numliberals):
            self.party_mem.append("Liberal")
        ### Shuffles the players, list with roles (party_mem) isn't shuffled
        for i in range(self.num_players):
            self.addplayer()
        random.shuffle(self.players)
        random.shuffle(self.players) ### To make sure it's Really shuffled
        random.shuffle(self.players)
        print(self.players)

            ### Create a deck
        for i in range(8):
            self.deck.append("Liberal")
        for i in range(11):
            self.deck.append("Facist")
        random.shuffle(self.deck)

        self.party_membership_view() ### To show each player their role

    def party_membership_view(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        self.next_ = input("Press Enter to continue.\n") ### Access to secret menu
        self.menu()
        for person in self.order_players:
            os.system('cls' if os.name == 'nt' else 'clear')
            self.pos = self.players.index(person)
            print(person)
            self.next_ = input("Press Enter to show role.") ### Gives spacing so player sees their own and not the next's
            print("\nYou are", self.party_mem[self.pos])
            self.next_ = input("Press Enter to continue.")  ### Gives spacing so player sees their own and not the next's
        self.rounds()

    def rounds(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        self.next_ = input("Press Enter to continue.\n") ### Access to secret menu
        self.menu()
        os.system('cls' if os.name == 'nt' else 'clear')
        ### President selection of cards
        draw = input("Draw cards(Press Enter)")
        print(self.deck[:3])
        selection = input("Discard a card(1, 2 or 3)\n")
        if selection.isnumeric() == True:    ### Error catching
            selection = int(selection)
            if selection < 1 or selection > 3:
                print("Invalid selection. Try again\n")
                self.rounds()
            selection -=1 ### Does this so it can be used as the index to move the item
            self.discard.append(self.deck[selection])
            self.deck.pop(selection)
            ### So Chancellor doesn't see President's selection
            os.system('cls' if os.name == 'nt' else 'clear')
            self.chancellor_selection()
        else:
            self.rounds()

        ### Chancellor selection of cards
    def chancellor_selection(self):
        print(self.deck[:2])
        self.selection = input("Discard a card(1 or 2)\n")
        if self.selection.isnumeric() == True:   ### Error catching
            self.selection = int(self.selection)
            if self.selection < 1 or self.selection > 2:
                print("Invalid selection. Try again\n")
                self.rounds()
            self.selection -=1 ### Does this so it can be used as the index to move the item
            self.discard.append(self.deck[self.selection])
            self.deck.pop(self.selection)
            if self.deck[0] == "Liberal":
                self.lib_board += 1
                print('number of fascist policies:', str(self.fac_board))
                print('number of liberal policies:', str(self.lib_board))
                if self.lib_board == 5:
                    print("End of game Liberals won")
                    self.output.close()
                    self.game_state = False
                    quit()
                else:
                    self.rounds()
            else:
                self.fac_board += 1
                print('number of fascist policies: ' + str(self.fac_board))
                print('number of liberal policies: ' + str(self.lib_board))
                if self.fac_board == 6:
                    print("End of game Facists won")
                    self.output.close()
                    self.game_state = False
                    quit()
                else:
                    self.president_powers()
        else:
            self.chancellor_selection()

    def president_powers(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("President's powers. Chancellor go away.\n")
        if self.fac_board == 1 or self.fac_board == 2:
            self.player_choice = input("Enter a player to investigate.\n").lower()
            if self.player_choice in self.players:    ### Check input is an actual player
                self.pos = self.players.index(self.player_choice)
                if self.party_mem[self.pos] == 'Secret Hitler':
                    print('Facist')         ### To not reveal Hitler's identity
                else:
                    print(self.party_mem[self.pos])
            else:
                print("Player is dead or not in player list. Try again.\n")
                self.president_powers()

        elif self.fac_board == 3:
            print("Choose the next President.\n")

        elif self.fac_board == 4 or self.fac_board == 5:
            player_choice = input("Choose a player to kill.\n").lower()
            if player_choice in self.players:
                self.pos = self.players.index(player_choice)
                if self.party_mem[self.pos] == "Secret Hitler":
                    print("End of game Liberals won")
                    game_state = False  ### End of game
                    quit()
                else:
                    self.players.pop(self.pos)    ### Removes player from list
                    self.party_mem.pop(self.pos)  ### Removes party membership from list
            else:
                self.president_powers()

        self.next_ = input("Press Enter for next round\n")
        os.system('cls' if os.name == 'nt' else 'clear')
        self.rounds()

    def menu(self):        ### Access to secret menu
        if self.next_ == "2002": ### Password to access menu
            self.choice = input("Menu:Change name of player(1)\nCheck role of a player(2)\nList players(3)\nList roles(4)\nExit(5)")
            if self.choice == "1":
                ### Removes old name and inserts new name
                self.current_name = input("Enter name of player whose name is to be changed.").lower()
                if self.current_name in self.players:
                    self.pos = self.players.index(self.current_name)
                    self.players.pop(self.pos)
                    self.new_name = input("Enter new name of player.").lower()
                    self.players.insert(self.pos,self.new_name)
                else:
                    print("Invalid input")
                    self.next_ = "2002" ### Return to top
                    self.menu()
            elif self.choice == "2":
                ### In case players forget
                self.name = input("Enter name of player whose role you want to check.")
                if self.name in self.players:
                    self.pos = self.players.index(self.name)
                    print(self.party_mem[self.pos])
                else:
                    print("Invalid input.\n")
                    self.next_ = "2002" ### Return to top
                    self.menu()
            elif self.choice == "3":
                ### To see players left
                print(self.players)
            elif self.choice == "4":
                ### To see how many roles are left
                print(self.party_mem)
            elif self.choice == "5":
                return
            else:
                print("Invalid input.\n")
                self.next_ = "2002" ### Return to top of function
                self.menu()
        else:
            return ### Back to function which called this one
        
    def get_board(self):
        return [self.lib_board, self.fac_board]

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