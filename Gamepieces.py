import pygame

def Gamepieces(screen,listx,listy):
  blackpawn = pygame.image.load('Chess_pdt60.png')

  for i in range (8):
    screen.blit(blackpawn, (listx[i],listy[1]))
