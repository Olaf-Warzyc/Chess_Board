import sys
from Gamepieces import Piece

import pygame
from pygame.locals import QUIT

global screen, width, height
global listx
global listy
listx = [] * 8
listy = [] * 8
pygame.init
width = 480
height = 480
clock = pygame.time.Clock()
background_colour = (255, 255, 255)  #set the backround colour
screen = pygame.display.set_mode((width, height))  # sets the
pygame.display.set_caption('Chess')
screen.fill(background_colour)  #fills the backround as white


def drawGrid():
  i = 0
  green = (0, 128, 0)
  white = (255, 255, 255)
  width_a = int(width / 8)
  height_a = int(height / 8)
  for x in range(0, width, width_a):
    for y in range(0, height, height_a):
      rect = pygame.Rect(x, y, width / 8, height / 8)
      if x not in listx:
        listx.append(x)
      if y not in listy:
        listy.append(y)
      if (i % 2 == 0):
        pygame.draw.rect(screen, white, rect, 0)
        i += 1
      else:
        pygame.draw.rect(screen, green, rect, 0)
        i += 1
    i -= 1

  return (listx, listy)
BP = Piece('b', 'p', 'BlackPawn.png')

"""def board(listx,llisty):
 board = {(0,0):pygame.image.load(BP.image)}
 """


print(listy, listx)




while True:
  drawGrid()
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()
  pygame.display.update()
