
import pygame

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = (255, 0, 0)  # Red color
        self.size = 100  # Size of the player square
        self.speed = 5  # Movement speed
        self.player_rect = pygame.Rect(self.x, self.y, self.size, self.size)

    def draw(self, screen):
        self.player_rect.topleft = self.x, self.y

        pygame.draw.rect(screen, self.color,self.player_rect)

        # if self.player_rect.bottomright == screen.get_width():
        #     self.x = screen.get_width() - 20

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def movements(self, keys):
        if keys[pygame.K_LEFT]:
            self.move(-1 * self.speed, 0)
        if keys[pygame.K_RIGHT]:
            self.move(self.speed, 0)
        if keys[pygame.K_UP]:
            self.move(0, -1 * self.speed)
        if keys[pygame.K_DOWN]:
            self.move(0, self.speed)
        
        # border collision
        
    def action(self, keys):
        if keys[pygame.K_SPACE]:
            self.speed = self.speed + 5
            print(self.speed)
        else:
            self.speed = 5

    def player_run(self, screen, keys):
        # draw the player
        self.draw(screen)

        # movements and actions
        self.action(keys)
        self.movements(keys)