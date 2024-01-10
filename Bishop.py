import pygame

from Gamepieces import Piece

class Bishop(Piece):
  def __init__(self, pos, colour, board):
    super().__init__(pos, colour, board)
    imagepath = 'Pieces/' + colour[0] + '_Bishop.png'
    self.img = pygame.image.load(imagepath)
    self.img = pygame.transform.scale(self.img, (board.tilewidth, board.tileheight ))
    self.notation = 'B'


  def getpossiblemove (self, board):
    output= []
    
    movene = []
    for i in range (1,8):
      if self.x +i >7 or self.y - i < 0 :
        break
      movene.append(board.squarepos((self.x +i, self.y - i )))
    output.append(movene)
    
    movese = []
    for i in range(1,8):
      if self.x + i >7 or self.y +i  >7:
        break
      movese.append(board.squarepos((self.x + i,self.y + i )))
    output.append(movese)
    
    movesw = []
    for i in range(1,8):
      if self.x - i < 0 or self.y + i >7:
        break
      movesw.append(board.squarepos((self.x - i, self.y + i)))
    output.append(movesw)
    
    movenw = []
    for i in range(1,8):
      if self.x -i < 0 or self.y- i < 0:
        break
      movenw.append(board.squarepos((self.x - i, self.y - i)))
    output.append(movenw)
    
    return output