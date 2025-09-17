import sys
import pygame

# my files

pygame.init()

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((800,600))
        pygame.display.set_caption("rouge like ")
        self.clock = pygame.time.Clock()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            
            pygame.display.update()
            self.clock.tick(60)
Game().run()