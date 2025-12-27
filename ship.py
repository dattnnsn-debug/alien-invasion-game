import pygame

class Ship: #Клас для керування корабля

    def __init__(self, ai_game):
        ''' Ініціювати корабель та задати його початкову позицію'''
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        '''Завантажити зображення корабля та отримати його текст'''
        self.image = pygame.image.load('images/ship.png')
        self.rect = self.image.get_rect()

        '''Створювати кожен новий корабель внизу екрана, по центру.'''
        self.rect.midbottom = self.screen_rect.midbottom

        '''Зберегти десяткове значення позиції корабля по горизонталі'''
        self.x = float(self.rect.x)

        '''Індикатор руху'''
        self.moving_right = False
        self.moving_left = False

    def update(self):
        '''Оновити поточну позицію корабля на основі індикатора руху.'''
        if self.moving_right:
            '''Оновити значення ship.x, а не rect.'''
            self.x += self.settings.ship_speed
        if self.moving_left:
            self.x -= self.settings.ship_speed

        '''Оновити об'єкт rect з self.x.'''
        self.rect.x = self.x

    def blitme(self):
        '''Намалювати корабель у його поточному розташуванні.'''
        self.screen.blit(self.image, self.rect)