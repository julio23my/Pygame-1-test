import pygame
import sys

pygame.init()

width = 400
height = 500


surface = pygame.display.set_mode((width,height)) # surface
pygame.display.set_caption('Colores')



# RGB
red = pygame.Color(255,0,0) # 0 - 255
green = pygame.Color(0,255,0)
blue = pygame.Color(0,0,255)

white = pygame.Color(255,255,255)
black = pygame.Color(0,0,0)

# Mediante Tuplas

my_color = (200,90,130)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() # salimos del juego
            sys.exit() ## terminamos el script

    surface.fill(my_color)
    pygame.display.update()