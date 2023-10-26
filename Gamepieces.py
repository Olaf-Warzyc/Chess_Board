import pygame

def Gamepieces(screen,listx,listy):
  blackpawn = pygame.image.load('Pawn Black.png')
  blackpawn = blackpawn.scale(0.5,0.5)

  for i in range (8):
    screen.blit(blackpawn, (listx[i],listy[1]-15))
