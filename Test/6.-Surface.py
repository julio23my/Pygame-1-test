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
blue = pygame.Color(59,87,181)

rect = pygame.Rect(100,150,120,60) # X, Y, Width, Height

rect.center = (width//2, height//2)

print(rect.x)
print(rect.y)

rect2 = (100,100,80,40)



surface2 = pygame.Surface((200,200))
surface2.fill(green)

rect = surface2.get_rect()
rect.center = (width//2,height//2)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() # salimos del juego
            sys.exit() ## terminamos el script

    surface.fill(white)
    surface.blit(surface2, rect)
    pygame.draw.rect(surface, red, (100,50,80,40))
    pygame.display.update()