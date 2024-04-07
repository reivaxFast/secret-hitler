import pygame, sys

class board:
    HOLDERS = (54, 52, 53)
    LIBERAL = pygame.image.load('liberal.png')
    FASCIST = pygame.image.load('fascist.png')
    def __init__(self, window: pygame.Surface) -> None:
        self.window = window
        self.cards = [0,0]

    def draw_cards(self):
        #element 1 in cards is number of fascists, element 2 is number of liberals
        for i in range(5):
            pygame.draw.rect(self.window, self.HOLDERS, pygame.Rect(25+(200 * i), 25, 165, 242), border_radius=10)
            if i<self.cards[0]:
                self.window.blit(self.LIBERAL, (20+(200 * i), 25))
        for i in range(6):
            pygame.draw.rect(self.window, self.HOLDERS, pygame.Rect(25+(200 * i), 300, 175, 245), border_radius=10)
            if i<self.cards[1]:
                self.window.blit(self.FASCIST, (25+(200 * i), 300))
    
    def add_card(self, card):
        if 'f' in card:
            self.cards[1] += 1
        else:
            self.cards[0] += 1


class screen:
    BACKGROUND = (9, 71, 15)
    def __init__(self):
        pygame.init()
        width, height = 1000, 500
        self.window = pygame.display.set_mode((width, height), pygame.RESIZABLE)
        self.board = board(self.window)
        pygame.display.set_caption("secret hitler")
    
    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        self.window.fill(self.BACKGROUND)
        self.board.draw_cards()
        pygame.display.flip()

    def run(self):
        while True:
            print('hi')
            self.update()

    def add_card(self, card):
        self.board.add_card(card)
