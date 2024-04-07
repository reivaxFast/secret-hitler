import display, time, threading

def test():
    global screen
    while type(screen) == int:
        print('no')
    for i in range(5):
        screen.add_card(input())
screen = display.screen()
t = threading.Thread(target= test)
t.start()
while True:
    screen.update()