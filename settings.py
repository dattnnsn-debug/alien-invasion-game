class Settings(object): #Клас для збереження всіх налаштувань гри.
    def __init__(self): #Ініціалізувати  постійні налаштування гри.
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (135, 206, 235)
        '''Налаштування корабля'''
        self.ship_speed = 1.5
        self.ship_limit = 3
        '''Налаштування кулі'''
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3
        '''Налаштування прибульця'''
        self.fleet_drop_speed = 10
        '''Як швидко гра має прискоритися'''
        self.speedup_scale = 1.1
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        '''Ініціалізація змінних налаштувань'''
        self.sheep_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0

        '''fleet_direction 1 представляє напрямок праворуч; -1 -- ліворуч'''
        self.fleet_direction = 1

    def increase_speed(self):
        '''Збільшення налаштувань швидкості'''
        self.sheep_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
