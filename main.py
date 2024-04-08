import display, threading, Secret_Hitler

screen = display.screen()
g = Secret_Hitler.game()
t = threading.Thread(target=g.game_start)
t.start()
while True:
    screen.update()
    screen.add_card(g.get_board())