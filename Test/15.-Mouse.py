import pygame
import sys

pygame.init()

width = 500
height = 600


surface = pygame.display.set_mode((width,height)) # surface
pygame.display.set_caption('Sonidos')



# RGB


white = pygame.Color(255,255,255)
red = pygame.Color(115,38,80)
green = pygame.Color(52,157,89)
blue = pygame.Color(59,87,181)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() # salimos del juego
            sys.exit() ## terminamos el script


        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_w]:
            print('Arriba')
        if pressed[pygame.K_s]:
            print('Abajo')
        if pressed[pygame.K_a]:
            print('Izquierda')
        if pressed[pygame.K_d]:
            print('Derecha')



    surface.fill(white)


    pygame.display.update()