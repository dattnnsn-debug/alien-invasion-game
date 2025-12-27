import pygame

class Space: #Клас для керування космос персонажем

    def __init__(self, ai_game):
        ''' Ініціювати космос та задати його початкову позицію'''
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        '''Завантажити зображення космосу та отримати його текст'''
        self.image = pygame.image.load('images/space.png')
        self.rect = self.image.get_rect()

        '''Створювати кожен космос  по центру.'''
        self.rect.center = self.screen_rect.center

    def blitme(self):
        '''Намалювати персонажа космос у його поточному розташуванні.'''
        self.screen.blit(self.image, self.rect)