import pygame

from Gamepieces import Piece


class Pawn(Piece):

  def __init__(self, pos, colour, board):
    super().__init__(pos, colour, board)
    imagepath = 'Pieces/' + colour[0] + '_Pawn.png'
    self.img = pygame.image.load(imagepath)
    self.img = pygame.transform.scale(
      self.img, (board.tilewidth - 5, board.tileheight - 5))
    self.notation = ' '

  def getpossiblemove(self,board):
    output = []
    moves = []
    
    #move foward
    if self.colour == 'white':
      moves.append((0, -1))
      if not self.hasmoved:
        moves.append((0, -2))
        
    elif self.colour == 'black':
      moves.append((0, 1))
      if not self.hasmoved:
        moves.append((0, 2))
        
    for move in moves:
      newpos = (self.x, self.y + move[1])
      if newpos[1] < 8 and newpos[1] >= 0:
        output.append(board.squarepos(newpos))
    return output

  def getmoves(self, board):
    output = []
    for square in self.getpossiblemove(board):
      if square.occupying != None:
        break
      else:
        output.append(square)
        
    if self.colour == 'white':
      if self.x + 1 < 8 and self.y - 1 >= 0:
        square = board.squarepos((self.x + 1, self.y - 1))
        if square.occupying != None:
          if square.occupying.colour != self.colour:
            output.append(square)
      if self.x -1 >= 0 and self.y >= 0:
        square = board.squarepos((self.x -1,self.y -1))
        if square.occupying != None:
          if square.occupying.colour != self.colour:
            output.append(square)
            
    elif self.colour == 'black':
      if self.x + 1 < 8 and self.y + 1 < 8:
        square = board.squarepos((self.x + 1, self.y + 1))
        if square.occupying != None:
          if square.occupying.colour != self.colour:
            output.append(square)
      if self.x - 1 >= 0 and self.y + 1 < 8:
        square = board.squarepos((self.x - 1, self.y + 1))
        if square.occupying != None:
          if square.occupying.colour != self.colour:
            output.append(square)
            
    return output

  def attackingsquare(self, board):
    moves = self.getmoves(board)
    return [i for i in moves if i.x != self.x]
