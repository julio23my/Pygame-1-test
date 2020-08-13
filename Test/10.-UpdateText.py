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

font = pygame.font.Font('freesansbold.ttf',48)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() # salimos del juego
            sys.exit() ## terminamos el script

    surface.fill(white)
    seconds = pygame.time.get_ticks()//1000
    text = font.render(str(seconds), True, red )
    rect = text.get_rect()
    rect.center = (width//2,height//2)

    surface.blit(text,rect)
    pygame.display.update()