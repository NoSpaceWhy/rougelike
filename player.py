
import pygame

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = (255, 0, 0)  # Red color
        self.size = 100  # Size of the player square
        self.speed = 5  # Movement speed
        

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.size, self.size))

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

    def action(self, keys):
        if keys[pygame.K_SPACE]:
            self.speed = self.speed + 5
            print(self.speed)
        else:
            self.speed = 5

    def player_camera(self, screen, keys):
        pass

    def player_run(self, screen, keys):
        # draw the player
        self.draw(screen)

        # movements and actions
        self.action(keys)
        self.movements(keys)
