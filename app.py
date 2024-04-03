import pygame
import game_config as gc
from pygame import display, event, image, transform
from animal import Animal

pygame.init()

display.set_caption('My Memory Game')
screen = display.set_mode((512, 512))

matched = image.load('other_assets/matched.png')
matched = transform.scale(matched, (512, 512))

running = True
tiles = [Animal(i) for i in range(0, gc.NUM_TILES_TOTAL)]

while running:
    # list of all keyboard and mouse events
    current_events = event.get()
    for e in current_events:
        # stop game if users quits
        if e.type == pygame.QUIT:
            running = False
    # initial blank screen
    screen.fill((255,255,255))
    # display animals
    for tile in tiles:
        screen.blit(tile.image, (tile.col * gc.IMAGE_SIZE, tile.row * gc.IMAGE_SIZE))
    display.flip()


print("Bye, bye!") 