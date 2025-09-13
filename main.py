import pygame

import player

pygame.init()

# screen dimensions and setup
screen_width = 800
screen_height = 700
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("RougeLike") #window title

clock = pygame.time.Clock() # fps controller
p = player.Player(400, 300)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.fill((0, 0, 0))

    keys = pygame.key.get_pressed()

    p.player_run(screen, keys)

    clock.tick(60)
    pygame.display.flip()