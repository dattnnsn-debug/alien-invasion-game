import sys

import pygame

from settings import Settings

from ship import Ship
from space_character import Space

class Alien_invasion: #Загальний клас, що керує ресурсами на поведінкою гри.'''

    def __init__(self):#Ініціалізувати гру, створити ресурс гри
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption('Alien Invasion')

        #Задати колір фону
        self.bg_color = (135, 206, 235)

        self.ship = Ship(self)

        self.space = Space(self)

    def run_game(self): #Розпочати головний цикл гри.
        while True:
            self._check_events()
            self._update_screen()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    '''Перемістити корабель праворуч'''
                    self.ship.rect.x += 1

    def _update_screen(self):
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()
            self.space.blitme()

            #Показати останній намальований екран.
            pygame.display.flip()
if __name__ == '__main__':
    #Створити екземпляр гри та запустити гру.
    ai = Alien_invasion()
    ai.run_game()