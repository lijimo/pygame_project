import pygame
from pygame import display, event

pygame.init()

display.set_caption('My Memory Game')
screen = display.set_mode((512, 512))
running = True

while running:
    # list of all keyboard and mouse events
    current_events = event.get()
    for e in current_events:
        # stop game if users quits
        if e.type == pygame.QUIT:
            running = False
print("Bye, bye!") 