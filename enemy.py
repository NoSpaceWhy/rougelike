import random
import pygame

import player

class Enemy:
    def __init__(self):
        self.x = 100
        self.y = 100
        self.speed = 100
        self.color = (0, 0, 255)
        self.size = 100
        self.enemy_rect = pygame.Rect(self.x, self.y, self.size, self.size)


    def enemy_spawn(self):
        self.x = 100
        self.y = 100

    def move(self):
        self.x += self.speed
        print(self.x)
    def enemy_draw(self, screen):
        self.enemy_rect.topleft = self.x, self.y

        pygame.draw.rect(screen, self.color, self.enemy_rect)


    def run(self, screen):
        self.enemy_spawn()
        self.enemy_draw(screen)