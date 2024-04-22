import random
from typing import override
import pygame
from pygame.locals import (
    RLEACCEL,
)


class Enemy(pygame.sprite.Sprite):
    def __init__(self, screen_width, screen_height):
        super(Enemy, self).__init__()
        self.surf = pygame.image.load("Bomber/Idle.png").convert_alpha()
        self.surf = pygame.transform.scale(self.surf, (50,50))
        self.surf = pygame.transform.rotate(self.surf, 180)
        self.surf.set_colorkey((255,255,255), RLEACCEL)
        self.rect = self.surf.get_rect(
            center=(
                random.randint(screen_width + 20, screen_width + 100),
                random.randint(0, screen_height)
            )
        )
        self.speed = random.randint(5,15)
    
    @override
    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()

