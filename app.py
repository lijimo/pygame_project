import pygame
import game_config as gc
from pygame import display, event, image, transform
from animal import Animal
from time import sleep

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
            if index not in current_images:
                current_images.append(index)
            # only display two animals at a time
            if len(current_images) > 2:
                current_images = current_images[1:]

    # initial blank screen
    screen.fill((255,255,255))

    total_skipped = 0

    # display animals
    for i, tile in enumerate(tiles):
        image_i = tile.image if i in current_images else tile.box
        if not tile.skip:
            screen.blit(image_i, (tile.col * gc.IMAGE_SIZE + gc.MARGIN, tile.row * gc.IMAGE_SIZE + gc.MARGIN))
        else:
            total_skipped += 1

    display.flip()
    
    # check for match
    if len(current_images) == 2:
        index1, index2 = current_images
        if tiles[index1].name == tiles[index2].name:
            tiles[index1].skip = True
            tiles[index2].skip = True
            sleep(0.5)
            screen.blit(matched, (0,0))
            display.flip()
            sleep(0.5)
            current_images = []
    
    if total_skipped == len(tiles):
        running = False

print("Bye, bye!") 