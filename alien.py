import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    '''Клас , що представляє одного прибульця від флоту'''
    def __init__(self, ai_game):
        '''Ініціювати прибульця, та задати його початкове розташування'''
        super().__init__()
        self.screen = ai_game.screen

        self.image = pygame.image.load('images/alien.png')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)