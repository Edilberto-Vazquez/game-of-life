import pygame
import numpy
from pygame.draw import polygon

pygame.init()

width, height = 1000, 1000
screen = pygame.display.set_mode((height, width))

bg = 25, 25, 25
screen.fill(bg)

nxC, nyC = 25, 25

dimCW = width / nxC
dimCW = height / nyC

while True:
    for y in range(0, nxC):
        for y in range(0, nyC):
            poly = [((x) * dimCW, y * dimCH),
                    ((x+1) * dimCW, y * dimCH),
                    ((x+1) * dimCW, (y+1) * dimCH),
                    ((x) * dimCW, y(y+1) * dimCH), ]
            pygame.draw.polygon(screen, (128, 128, 128, poly, 1))

    pygame.display.flip()
