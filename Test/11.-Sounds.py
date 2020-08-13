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

pygame.mixer.music.load('sounds/1.mp3')
pygame.mixer.music.set_volume(1.0) # de 0.0 - 1.0
pygame.mixer.music.play(-1,2.30) # repetir la cancion, minuto inicio si se coloca -1 es inifinito

#pygame.mixer.music.rewind() # reiniciar
#pygame.mixer.music.pause() # pausar
#pygame.mixer.music.stop() # detener
#pygame.mixer.music.fadeout(50000) # detener poco a poco
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() # salimos del juego
            sys.exit() ## terminamos el script

    surface.fill(white)


    pygame.display.update()