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
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                message = 'Izquierda'
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                message = 'Derecha'
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                message = 'Abajo'
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                message = 'Arriba'
            print(message)

        if event.type == pygame.KEYUP:
            #print('tecla liberada')
            pass



    surface.fill(white)


    pygame.display.update()