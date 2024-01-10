import pygame 
from Gamepieces import Piece

class King(Piece):
  def __init__(self, pos, colour, board):
    super().__init__(pos, colour, board) 
    imagepath = 'Pieces/' + colour[0] + '_King.png'
    self.img = pygame.image.load(imagepath)
    self.img = pygame.transform.scale(self.img, (board.tilewidth , board.tileheight))
    self.notation = 'K'


  def getpossiblemove(self,board):
    output = []
    moves = [(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1)]
    #north,ne,east,se,south,sw,west,nw
    for move in moves:
      newpos = (self.x + move[0], self.y + move[1])
      if (newpos[0] < 8 and newpos[0] >= 0 and newpos[1] < 8 and newpos[1] >= 0 ):
        output.append([board.squarepos(newpos)])
    return output

  def cancastle(self,board):
    if not self.hasmoved:
      
      if self.colour == 'white':
        Queensiderook = board.piecepos((0,7))
        Kingsiderook = board.piecepos((7,7))
        if Queensiderook != None:
          if not Queensiderook.hasmoved:
            if [board.piecepos((i,7)) for i in range (1, 4)] == [None,None,None]:
              return 'queenside'
        if Kingsiderook != None:
          if not Kingsiderook.hasmoved:
            if[board.piecepos((i,7)) for i in range (5,7)] == [None,None]:
              return 'kingside'
              
      elif self.colour == 'black':
        Queensiderook = board.piecepos((0,0))
        Kingsiderook = board.piecepos((7,0))
        if Queensiderook != None:
          if not Queensiderook.hasmoved:
            if [board.piecepos((i,0)) for i in range (1,4)] == [None, None, None]:
              return 'queenside'
        if Kingsiderook != None:
          if not Kingsiderook.hasmoved:
            if [ board.piecepos((i,0)) for i in range(5,7)] == [None, None]:
              return 'kingside'

  def getvalidmove(self, board): 
    output = []
    for square in self.getmoves(board):
      if not board.is_in_check(self.colour,boardchange = [self.pos, square.pos]):
        output.append(square)
        
    if self.cancastle(board) == 'queenside':
      output.append(board.squarepos((self.x -2,self.y)))
      
    if self.cancastle(board) == 'kingside':
      output.append(board.squarepos((self.x +2,self.y)))
    
    return output