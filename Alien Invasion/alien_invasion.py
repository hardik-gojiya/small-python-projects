import sys
import pygame
from setting import settings
from ship import Ship
from bullet import Bullet
from alien import Alien


class AlienInvasion:

    def __init__(self):
        pygame.init()
        self.settings = settings()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)

        self.bullet = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        
        self._create_fleet()

    def _create_fleet(self):
        alien = Alien(self)
        self.aliens.add(alien)
    
    def runGame(self):
        while True:
            self.check_events()
            self.ship.update()
            self.update_bullet()
            self.update_screen()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.quit:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
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

    def update_bullet(self):
        self.bullet.update()
        for bullet in self.bullet.copy():
            if bullet.rect.bottom <= 0:
                self.bullet.remove(bullet)

    def update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        for bullet in self.bullet.sprites():
            bullet.draw()
        
        self.aliens.draw(self.screen)
        pygame.display.flip()
        
        
    def _fire_bullet(self):
        if len(self.bullet) < self.settings.bullet_allowed:
            new_bullet = Bullet(self)
            self.bullet.add(new_bullet)


if __name__ == "__main__":
    ai = AlienInvasion()
    ai.runGame()
