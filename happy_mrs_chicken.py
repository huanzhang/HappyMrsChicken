#!/usr/bin/env python

import pygame, sys, random, time
from pygame.locals import *

pygame.init()
DISPLAYSURF = pygame.display.set_mode((960, 720))
pygame.display.set_caption('Hello World!')

WHITE = (0, 0, 255)
DISPLAYSURF.fill(WHITE)

backdrop = pygame.image.load('backdrop.png')

chickens = [pygame.image.load('hmc.png'), pygame.image.load('hmc2.png')]
chicken_position = (random.randint(0, 960-157), random.randint(0, 720-195))
chicken_number = 0
IMAGE_TIME = 20

clock = pygame.time.Clock()
while True: # main game loop
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYUP:
            if event.key == K_SPACE:
                chicken_position = (random.randint(0, 960-157), random.randint(0, 720-195))

    if IMAGE_TIME > 0:
        IMAGE_TIME -= 1
    else:
        IMAGE_TIME = 20
        chicken_number ^= 1

    DISPLAYSURF.blit(backdrop, (0, 0))
    DISPLAYSURF.blit(chickens[chicken_number], chicken_position)


    pygame.display.update()
