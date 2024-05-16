import pygame, sys

class board:
    def __init__(self, window: pygame.Surface, num) -> None:
        self.window = window
        self.num_players = num
        self.cards = [0,0]
        self.HOLDERS = (54, 52, 53)
        self.LIBERAL = pygame.transform.scale_by(pygame.image.load('images/liberal.png'), 0.85)
        self.FASCIST = pygame.transform.scale_by(pygame.image.load('images/fascist.png'), 0.85)
        self.B5 = pygame.transform.scale_by(pygame.image.load('images/5-6.png'), 0.7)
        self.B7 = pygame.transform.scale_by(pygame.image.load('images/7-8.png'), 0.7)
        self.B9 = pygame.transform.scale_by(pygame.image.load('images/9-10.png'), 0.7)
        self.LIB = pygame.transform.scale_by(pygame.image.load('images/lib.png'), 0.7)
        self.lib_alpha = 255
        self.fasc_alpha = 255
        self.ch_lib = 0
        self.ch_fas = 0

    def draw_cards(self):
        #element 1 in cards is number of fascists, element 2 is number of liberals
        self.scale = min(self.window.get_size()[1]/1009, self.window.get_size()[0]/1250)
        self.liberal = pygame.transform.scale_by(self.LIBERAL, self.scale)
        self.fascist = pygame.transform.scale_by(self.FASCIST, self.scale)
        self.b5 = pygame.transform.scale_by(self.B5, self.scale)
        self.b7 = pygame.transform.scale_by(self.B7, self.scale)
        self.b9 = pygame.transform.scale_by(self.B9, self.scale)
        self.lib = pygame.transform.scale_by(self.LIB, self.scale)
        if self.num_players < 7:
            self.window.blit(self.b5, (35 * self.scale, 500 * self.scale))
        elif self.num_players < 9:
            self.window.blit(self.b7, (35 * self.scale, 500 * self.scale))
        else:
            self.window.blit(self.b9, (35 * self.scale, 500 * self.scale))
        self.window.blit(self.lib, (35 * self.scale, 20 * self.scale))
        for i in range(5):
            self.liberal.set_alpha(255)
            if i<self.cards[0]-1:
                self.window.blit(self.liberal, ((245 * self.scale)+(160 * i * self.scale), 147 * self.scale))
            elif i < self.cards[0]:
                self.liberal.set_alpha(self.lib_alpha)
                self.window.blit(self.liberal, ((245 * self.scale)+(160 * i * self.scale), 147 * self.scale))
        for i in range(6):
            self.fascist.set_alpha(255)
            if i<self.cards[1]-1:
                self.window.blit(self.fascist, ((162 * self.scale)+(160 * i * self.scale), 628 * self.scale))
            elif i < self.cards[1]:
                self.fascist.set_alpha(self.fasc_alpha)
                self.window.blit(self.fascist, ((162 * self.scale)+(160 * i * self.scale), 628 * self.scale))
        self.lib_alpha = min(self.lib_alpha+self.ch_lib, 255)
        self.fasc_alpha = min(self.fasc_alpha+self.ch_fas, 255)
        self.ch_lib *= 1.02
        self.ch_fas *= 1.02
    
    def add_card(self, card):
        if self.cards[0] != card[0]:
            self.lib_alpha = 0
            self.ch_lib = 0.01
        elif self.cards[1] != card[1]:
            self.fasc_alpha = 0
            self.ch_fas = 0.01
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
                return True
        self.window.fill(self.BACKGROUND)
        self.board.draw_cards()
        pygame.display.flip()
        return False

    def run(self):
        while True:
            print('hi')
            self.update()

    def add_card(self, card):
        self.board.add_card(card)
    
    def end(self):
        pygame.quit()
        sys.exit()
