import sys

import pygame

from settings import Settings

class Alien_invasion: #Загальний клас, що керує ресурсами на поведінкою гри.'''

    def __init__(self):#Ініціалізувати гру, створити ресурс гри
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption('Alien Invasion')

        #Задати колір фону
        self.bg_color = (230, 230, 230)

    def run_game(self): #Розпочати головний цикл гри.
        while True:
            #Слідкувати за подіями миші та клавіатури
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            #Наново перемалювати екран на кожній ітерації циклу
            self.screen.fill(self.settings.bg_color)

            #Показати останній намальований екран.
            pygame.display.flip()
if __name__ == '__main__':
    #Створити екземпляр гри та запустити гру.
    ai = Alien_invasion()
    ai.run_game()