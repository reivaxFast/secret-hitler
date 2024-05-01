import pygame, sys

class board:
    HOLDERS = (54, 52, 53)
    LIBERAL = pygame.transform.scale_by(pygame.image.load('images/liberal.png'), 0.85)
    FASCIST = pygame.transform.scale_by(pygame.image.load('images/fascist.png'), 0.85)
    B5 = pygame.transform.scale_by(pygame.image.load('images/5-6.png'), 0.7)
    B7 = pygame.transform.scale_by(pygame.image.load('images/7-8.png'), 0.7)
    B9 = pygame.transform.scale_by(pygame.image.load('images/9-10.png'), 0.7)
    lib = pygame.transform.scale_by(pygame.image.load('images/lib.png'), 0.7)
    def __init__(self, window: pygame.Surface, num) -> None:
        self.window = window
        self.num_players = num
        self.cards = [0,0]

    def draw_cards(self):
        #element 1 in cards is number of fascists, element 2 is number of liberals
        if self.num_players < 7:
            self.window.blit(self.B5, (35, 500))
        elif self.num_players < 9:
            self.window.blit(self.B7, (35, 500))
        else:
            self.window.blit(self.B9, (35, 500))
        self.window.blit(self.lib, (35, 20))
        for i in range(5):
            if i<self.cards[0]:
                self.window.blit(self.LIBERAL, (245+(160 * i), 147))
        for i in range(6):
            if i<self.cards[1]:
                self.window.blit(self.FASCIST, (162+(160 * i), 628))
    
    def add_card(self, card):
        self.cards = card


class screen:
    BACKGROUND = (48, 47, 47)
    def __init__(self, num):
        pygame.init()
        img = pygame.image.load('images/icon.svg')
        pygame.display.set_icon(img) 
        width, height = 1000, 500
        self.window = pygame.display.set_mode((width, height), pygame.RESIZABLE)
        self.board = board(self.window, num)
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
