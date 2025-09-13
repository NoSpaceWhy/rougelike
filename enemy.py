import random
import pygame

import player

class Enemy:
    def __init__(self):
        self.x
        self.y
        self.speed = 3
        self.colour = (0, 255, 0)
        self.size = 100
        self.enemy_rect = pygame.Rect(self.x, self.y, self.size, self.size)

        self.p = player.Player()

    def enemy_spawn(self):
        self.x = 100
        self.y = 100

    
    def enemy_ai(self):
        self.p.get_player()
        