import display, threading, Secret_Hitler

g = Secret_Hitler.game()
t = threading.Thread(target=g.game_start)
t.start()
while g.num_players == 0:
    pass
screen = display.screen(g.num_players)
while True:
    if screen.update():
        g.end()
        screen.end()
    screen.add_card(g.get_board())