import random
from enemy import Enemy
from cloud import Cloud
from player import Player
from typing import override
import pygame
from pygame.locals import (
    K_ESCAPE,
    KEYDOWN,
    QUIT
)
pygame.init()


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

clock = pygame.time.Clock()

# create custom event for adding enemies
ADD_ENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADD_ENEMY, 250)
ADD_CLOUD = pygame.USEREVENT + 2
pygame.time.set_timer(ADD_CLOUD, 1000)

player = Player(SCREEN_WIDTH, SCREEN_HEIGHT)

enemy_sprites = pygame.sprite.Group()
clouds = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

running = True
while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False
        elif event.type == ADD_ENEMY:
            new_enemy = Enemy(SCREEN_WIDTH, SCREEN_HEIGHT)
            enemy_sprites.add(new_enemy)
            all_sprites.add(new_enemy)
        elif event.type == ADD_CLOUD:
            new_cloud = Cloud(SCREEN_WIDTH, SCREEN_HEIGHT)
            clouds.add(new_cloud)
            all_sprites.add(new_cloud)


    pressed_keys = pygame.key.get_pressed()
    player.update(pressed_keys)

    enemy_sprites.update()

    clouds.update()

    screen.fill((135,206,235))

    surf_center = (
        (SCREEN_WIDTH-player.surf.get_width())/2,
        (SCREEN_HEIGHT-player.surf.get_height())/2
    )

    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)

    if pygame.sprite.spritecollideany(player, enemy_sprites):
        player.kill()
        running = False

    pygame.display.flip()

    clock.tick(30)

pygame.quit()

