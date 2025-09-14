import random
import pygame

import player

class Enemy:
    def __init__(self):
        self.x = 100
        self.y = 100
        self.speed = 3
        self.color = (0, 0, 255)
        self.size = 100
        self.enemy_rect = pygame.Rect(self.x, self.y, self.size, self.size)

        self.p = player.Player()

    def enemy_spawn(self):
        self.x = 100
        self.y = 100

    
    def enemy_ai(self):
        self.p.get_player()
        self.x += 5
    
    def enemy_draw(self, screen):
        self.enemy_rect.topleft = self.x, self.y
        self.enemy_ai()

        pygame.draw.rect(screen, self.color, self.enemy_rect)


    def run(self, screen):
        self.enemy_spawn()

        
        
        self.enemy_draw(screen)
