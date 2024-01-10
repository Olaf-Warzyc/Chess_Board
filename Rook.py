import pygame
from Gamepieces import Piece

class Rook (Piece):
  def __init__(self, pos, colour, board):
    super().__init__(pos, colour, board)
    imagepath = 'Pieces/' + colour[0] + '_Rook.png'
    self.img = pygame.image.load(imagepath)
    self.img = pygame.transform.scale(self.img, (board.tilewidth, board.tileheight))
    self.notation = 'R'

  def getpossiblemove(self,board):
    output = []
    
    movenorth = []
    for y in range(self.y)[::-1]:
      movenorth.append(board.squarepos((self.x,y)))
    output.append(movenorth)
    
    moveeast = []
    for x in range(self.x + 1,8):
      moveeast.append(board.squarepos((x,self.y)))
    output.append(moveeast)
    
    movesouth = []
    for y in range(self.y +1,8):
      movesouth.append(board.squarepos((self.x,y)))
    output.append(movesouth)
    
    movewest = []
    for x in range(self.x)[::-1]:
      movewest.append(board.squarepos((x,self.y)))
    output.append(movewest)
    
    return output
    