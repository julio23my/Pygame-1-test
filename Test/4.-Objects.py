import pygame
import sys

pygame.init()

width = 400
height = 500


surface = pygame.display.set_mode((width,height)) # surface
pygame.display.set_caption('rectangulos')



# RGB


white = pygame.Color(255,255,255)
red = pygame.Color(115,38,80)
green = pygame.Color(52,157,89)

rect = pygame.Rect(100,150,120,60) # X, Y, Width, Height

rect.center = (width//2, height//2)

print(rect.x)
print(rect.y)

rect2 = (100,100,80,40)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() # salimos del juego
            sys.exit() ## terminamos el script

    surface.fill(white)
    #draw el orden si importa
    # 1.- Donde se pinta la figura
    # 2.- Color que tendra la figura
    pygame.draw.rect(surface, red, (100,100,80,40))
    pygame.draw.circle(surface, green, (200,300), 100)
    pygame.draw.line(surface, red, (100,100), (200,300), 2)


    pygame.display.update()