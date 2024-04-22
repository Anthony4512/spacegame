import random
from typing import override
import pygame
from pygame.locals import (
    RLEACCEL,
)

class Cloud(pygame.sprite.Sprite):
    def __init__(self, screen_width, screen_height):
        super(Cloud, self).__init__()
        self.surf = pygame.image.load("cloud1.png").convert_alpha()
        self.surf = pygame.transform.scale(self.surf, (110,80))
        self.surf.set_colorkey((255,255,255), RLEACCEL)
        self.rect = self.surf.get_rect(
            center=(
                random.randint(screen_width + 20, screen_width + 100),
                random.randint(0, screen_height)

            )
        )

    @override
    def update(self):
        self.rect.move_ip(-5, 0)
        if self.rect.right < 0:
            self.kill()
            
