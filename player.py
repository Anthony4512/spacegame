from typing import override
import pygame
from pygame.locals import (
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
)


class Player(pygame.sprite.Sprite):
    def __init__(self, screen_width, screen_height):
        super(Player, self).__init__()
        self.surf = pygame.image.load("Corvette/Idle.png").convert_alpha()
        self.surf = pygame.transform.scale(self.surf, (50,50))
        self.surf.set_colorkey((255,255,255), RLEACCEL)
        self.rect = self.surf.get_rect()
        self.screen_width = screen_width
        self.screen_height = screen_height

    @override
    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)

        # make it not go offscreen
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= self.screen_height:
            self.rect.bottom = self.screen_height
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.right >= self.screen_width:
            self.rect.right = self.screen_width

