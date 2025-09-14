import pygame
import pytmx

import player
import enemy

pygame.init()

# screen dimensions and setup
screen_width = 800
screen_height = 700
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("RougeLike") #window title

clock = pygame.time.Clock() # fps controller

# map
scale = 2
tmx_data = pytmx.util_pygame.load_pygame("maps/map.tmx")
map_width = tmx_data.width
map_height = tmx_data.height

tile_width = tmx_data.tilewidth * scale
tile_height = tmx_data.tileheight * scale

map_width = map_width * tile_width
map_height = map_height * tile_height

# player
p = player.Player(400, 300)
e = enemy.Enemy()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.fill((0, 0, 0))

    keys = pygame.key.get_pressed()


    # map code
    for layer in tmx_data.visible_layers:
        if isinstance(layer, pytmx.TiledTileLayer):
            for x, y, gid in layer:
                tile = tmx_data.get_tile_image_by_gid(gid)
                if tile:
                    screen.blit(tile, (x * tile_width, y * tile_height))

    e.run(screen)
    e.move()

    p.player_run(screen, keys)


    clock.tick(60)
    pygame.display.flip()