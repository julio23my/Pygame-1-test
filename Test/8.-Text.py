import pygame
import sys

pygame.init()

width = 500
height = 600


surface = pygame.display.set_mode((width,height)) # surface
pygame.display.set_caption('Imagenes')



# RGB


white = pygame.Color(255,255,255)
red = pygame.Color(115,38,80)
green = pygame.Color(52,157,89)
blue = pygame.Color(59,87,181)

#1- obtener fuente

font = pygame.font.Font('freesansbold.ttf',48)

#2.- Crear el texto

text = font.render('Hola mundo!',True, red) # -> surface
rect = text.get_rect()
rect.center = (width//2, height//2)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() # salimos del juego
            sys.exit() ## terminamos el script

    surface.fill(white)
    surface.blit(text,rect)
    pygame.display.update()