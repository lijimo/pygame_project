import pygame
import game_config as gc
from pygame import display, event, image, transform
from animal import Animal

def find_index(x, y):
    row = y // gc.IMAGE_SIZE
    col = x // gc.IMAGE_SIZE
    index = row * gc.NUM_TILES_SIDE + col
    return index

pygame.init()

display.set_caption('My Memory Game')
screen = display.set_mode((512, 512))

matched = image.load('other_assets/matched.png')
matched = transform.scale(matched, (512, 512))

running = True
tiles = [Animal(i) for i in range(0, gc.NUM_TILES_TOTAL)]
current_images = []

while running:
    # list of all keyboard and mouse events
    current_events = event.get()
    for e in current_events:
        # stop game if users quits
        if e.type == pygame.QUIT:
            running = False
        if e.type == pygame.K_ESCAPE:
            running = False
        # check mouse position
        if e.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            index = find_index(mouse_x, mouse_y)
            current_images.append(index)

    # initial blank screen
    screen.fill((255,255,255))
    # display animals
    for tile in tiles:
        screen.blit(tile.image, (tile.col * gc.IMAGE_SIZE + gc.MARGIN, tile.row * gc.IMAGE_SIZE + gc.MARGIN))
    
    display.flip()

print("Bye, bye!") 