import pygame

from Gamepieces import Piece

class Queen(Piece):
  def __init__(self, pos, colour, board):
    super().__init__(pos, colour, board)
    imagepath = 'Pieces/' + colour[0] + '_Queen.png'
    self.img = pygame.image.load(imagepath)
    self.img = pygame.transform.scale(self.img, (board.tilewidth, board.tileheight))
    self.notation = 'Q'

  def getpossiblemove(self,board):
    output = []
    
    movenorth = []
    for y in range(self.y) [::-1]:
      movenorth.append(board.squarepos((self.x,y)))
    output.append(movenorth)
    
    movene = []
    for i in range(1,8):
      if self.x + i>7 or self.y -i < 0:
        break
      movene.append(board.squarepos((self.x +i ,self.y - i)))
    output.append(movene)
    
    moveeast = []
    for x in range(self.x + 1,8):
      moveeast.append(board.squarepos((x,self.y)))
    output.append(moveeast)
    
    movese = []
    for i in range(1,8):
      if self.x+i > 7or self.y +i>7:
        break
      movese.append(board.squarepos((self.x + i,self.y +i)))
    output.append(movese)
      
    movesouth = []
    for y in range(self.y + 1, 8):
      movesouth.append(board.squarepos((self.x,y)))
    output.append(movesouth)
      
    movesw = []
    for i in range(1,8):
      if self.x -i < 0 or self.y + i >7:
        break
      movesw.append(board.squarepos((self.x - i,self.y + i )))
    output.append(movesw)
      
    movewest = []
    for x in range(self.x)[::-1]:
      movewest.append(board.squarepos((x,self.y)))
    output.append(movewest)
      
    movenw =[]
    for i in range(1,8):
      if self.x - i < 0 or self.y - i < 0:
        break
      movenw.append(board.squarepos((self.x - i, self.y - i)))
    output.append(movenw)
      
    return output
      