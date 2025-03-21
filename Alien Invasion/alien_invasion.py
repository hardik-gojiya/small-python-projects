import sys
import pygame
from setting import settings


class AlienInvasion:

    def __init__(self):
        pygame.init()
        self.settings = settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption("Alien Invasion")

    def runGame(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.quit:
                    sys.exit()

            self.screen.fill(self.settings.bg_color)

            pygame.display.flip()


if __name__ == "__main__":
    ai = AlienInvasion()
    ai.runGame()
