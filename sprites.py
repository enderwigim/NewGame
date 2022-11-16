import pygame
import os
from engine import *


class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()

        self.image = pygame.transform.scale(pygame.image.load(os.path.join("Assets/Characters", "Annie.png")),
                                            (PLAYER_WIDTH, PLAYER_HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]

    def update(self, key_pressed):
        if key_pressed[pygame.K_a] and self.rect.x > 0:  # Left
            self.rect.x -= 1
        if key_pressed[pygame.K_d] and self.rect.x < WIDTH - PLAYER_WIDTH: # Right
            self.rect.x += 1
        if key_pressed[pygame.K_s] and self.rect.y < HEIGHT - PLAYER_HEIGHT: # Down
            self.rect.y += 1
        if key_pressed[pygame.K_w] and self.rect.y > 0: # Up
            self.rect.y -= 1

class Wall(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.image = pygame.Surface((TILESIZE, TILESIZE))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.x = pos_x
        self.y = pos_y
        self.rect.x = pos_x * TILESIZE
        self.rect.y = pos_y * TILESIZE

