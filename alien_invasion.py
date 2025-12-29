import sys

from time import sleep

import pygame

from settings import Settings

from game_stats import GameStats

from ship import Ship

from bullet import Bullet

from alien import Alien


class Alien_invasion: #Загальний клас, що керує ресурсами на поведінкою гри.'''

    def __init__(self):#Ініціалізувати гру, створити ресурс гри
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

        pygame.display.set_caption('Alien Invasion')

        '''Створити екземпляр для збереження ігрової статистики'''
        self.stats = GameStats(self)

        #Задати колір фону
        self.bg_color = (135, 206, 235)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

        '''Розпочати гру в активиному стані'''
        self.game_active = True

    def run_game(self): #Розпочати головний цикл гри.
        while True:
            self._check_events()
            if(self.stats.game_active):
                self.ship.update()
                self._update_bullets()
                self._update_aliens()

            self._update_screen()

    def _check_events(self):
        '''Реагувати на натискання клавіш та події миші'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)


    def _check_keydown_events(self, event):
        '''Реагування на натискання клавіш'''
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        '''Створи нову кулю та додай її до групи куль'''
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        '''ОНовити позиції куль та позбавитися старих куль'''
        self.bullets.update()

        '''Перевірити чи якась із куль не влучила у прибульця.
        Якщо влучила, позбравитися кулі і прибульця'''

        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

        '''Позбавитися куль, що зникли'''
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <=0:
                self.bullets.remove(bullet)

        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        '''Реакція на зіткнення куль з прибульцями
        Видалити всі кулі та прибульців, що зіткнулися'''
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

        if not self.aliens:
            '''Знищити кулі та створити новий флот'''
            self.bullets.empty()
            self._create_fleet()

    def _update_aliens(self):
        '''Перевірити чи флот знаходиться на краю, тоді оновити позиції всіх прибульців флоту'''
        self._check_fleet_edges()
        self.aliens.update()

        '''Шукати зіткнення куль з прибульцями'''
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

            '''Шукати, чи котрийсь із прибульців досяг нижнього краю екрану'''
        self._check_aliens_bottom()

    def _create_fleet(self):
        '''Створити злот прибульця з 1 кораблем'''
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)

        '''Визначити яка кількість рядів прибульців поміщається на екрані.'''
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height -
                             (3 * alien_height) - ship_height)
        numer_rows = available_space_y // (2 * alien_height)

        '''Створити повний флот прибульців'''
        for row_number in range(numer_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):

        '''Сторити прибульця і поставити його до ряду'''
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

    def _check_fleet_edges(self):
        '''Реагує відповідно до того чи досягкотийсь із прибульців краю екрана'''

        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        '''Спуск всього флоту та зміна його напрямку.'''
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _ship_hit(self):
        '''Реагуваня на зіткнення корабля з прибульцем
        Зменшити ship left'''
        if self.stats.ships_left > 0:
            self.stats.ships_left -= 1
            self.aliens.empty()
            self.bullets.empty()
            self._create_fleet()
            self.ship.center_ship()
            sleep(0.5)
        else:
            self.stats.game_active = False

    def _check_aliens_bottom(self):
        '''Перевіряти, чи не досяг якийсь прибулець нижнього краю екрану'''
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                '''Зреагувати так, ніби корабель підбито'''
                self._ship_hit()
                break


    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)

        #Показати останній намальований екран.
        pygame.display.flip()
if __name__ == '__main__':
    #Створити екземпляр гри та запустити гру.
    ai = Alien_invasion()
    ai.run_game()