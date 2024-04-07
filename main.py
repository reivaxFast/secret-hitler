import display, threading, Secret_Hitler

def test():
    global screen
    while type(screen) == int:
        print('no')
    for i in range(5):
        screen.add_card(input())
screen = display.screen()
g = Secret_Hitler.game()
t = threading.Thread(target=g.game_start)
t.start()
while True:
    screen.update()
    screen.add_card(g.get_board())