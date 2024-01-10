import pygame 

from Gamepieces import Piece

class Knight(Piece):
  def __init__(self, pos, colour, board):
    super().__init__(pos, colour, board)
    imagepath = 'Pieces/' + colour[0] +'_Knight.png'
    self.img = pygame.image.load(imagepath)
    self.img = pygame.transform.scale(self.img, (board.tilewidth, board.tileheight))
    self.notation = 'N'

  def getpossiblemove (self,board):
    output = []
    moves = [(1,-2),(2,-1),(2,1),
             (1,2),(-1,2),(-2,1),
             (-2,-1),(-1,-2)]
    for move in moves:
      newpos = (self.x + move[0], self.y + move[1])
      if (newpos[0] < 8 and newpos[0] >= 0 and
         newpos[1] < 8 and newpos[1] >= 0):
        output.append([board.squarepos(newpos)])
        
    return output
    
  