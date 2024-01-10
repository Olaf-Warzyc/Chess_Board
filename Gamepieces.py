import pygame

class Piece:
  def __init__(self, pos, colour, board ):
    self.pos = pos
    self.x = pos[0]
    self.y = pos[1]
    self.colour = colour
    self.hasmoved = False
 
  def getmoves(self,board):
    output =[]
    for direction in self.getpossiblemove(board):
      for square in direction:
        if square.occupying is not None:
          if square.occupying.colour == self.colour:
            break
          else:
            output.append(square)
            break
        else:
          output.append(square)
    return output
  
  def getvalidmove(self, board):
    output = []
    for square in self.getmoves(board):
      if not board.is_in_check(self.colour, boardchange = [self.pos, square.pos]):
        output.append(square)
    return output


  def move(self, board, square, force=False):
    for i in board.squares:
      i.highlight = False 
      
    if square in self.getvalidmove(board) or force:
      prevsquare = board.squarepos(self.pos)
      self.pos,self.x,self.y = square.pos, square.x, square.y
      
      prevsquare.occupying = None
      square.occupying = self
      board.selectedpiece = None
      self.hasmoved = True
      
      #pawn promotion 
      if self.notation == ' ':
        if self.y == 0 or self.y == 7:
          from Queen import Queen
          square.occupying = Queen((self.x, self.y),self.colour,board)
          
      #rook castle 
      if self.notation == 'K':
        if prevsquare.x - self.x == 2:
          rook = board.piecepos((0,self.y))
          rook.move(board, board.squarepos((3,self.y)),force = True)
        elif prevsquare.x - self.x == -2 :
          rook = board.piecepos((7, self.y))
          rook.move(board, board.squarepos((5,self.y)), force = True)
      return True
    else:
      board.selectedpiece = None
      return False

  def attackingsquare(self, board):
    return self.getmoves(board)