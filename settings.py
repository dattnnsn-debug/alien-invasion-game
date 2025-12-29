class Settings(object): #Клас для збереження всіх налаштувань гри.
    def __init__(self): #Ініціалізувати налаштування гри.
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (135, 206, 235)
        '''Налаштування корабля'''
        self.ship_speed = 1.5
        self.sheep_limit = 3
        '''Налаштування кулі'''
        self.bullet_speed = 1.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3
        '''Налаштування прибульця'''
        self.alien_speed = 1.0
        self.fleet_drop_speed = 100
        '''fleet_direction 1 означає напрямок руху праворуч; -1 -- ліворуч'''
        self.fleet_direction = 1
