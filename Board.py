import pygame

from Square import Square
from Rook import Rook
from Bishop import Bishop
from Knight import Knight
from Queen import Queen
from King import King
from Pawn import Pawn
#would also import all the pieces data here


class Board:
  def __init__ (self, width, height):
    self.width = width
    self.hieght = height
    self.tilewidth = width//8
    self.tileheight = height//8
    self.selectedpiece = None
    self.turn = 'white'
    self.config =[ 
    ['bR', 'bN', 'bB', 'bQ', 'bK', 'bB', 'bN', 'bR'],
    ['bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP'],
    ['','','','','','','',''],
    ['','','','','','','',''],
    ['','','','','','','',''],
    ['','','','','','','',''],
    ['wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP'],
    ['wR', 'wN', 'wB', 'wQ', 'wK', 'wB', 'wN', 'wR'],]
    self.squares = self.generate_squares()
    self.setup()



  def generate_squares(self):
    output = [] #calls an empty list 
    for y in range(8): 
        for x in range(8): #8 by 8 squares 
            output.append(Square(x,  y, self.tilewidth, self.tileheight))
    return output

  def squarepos(self,pos) :
    for square in self.squares:
      if (square.x, square.y) == (pos[0], pos[1]):
        return square

  def piecepos(self, pos):
    return self.squarepos(pos).occupying


  def setup(self):
    for y, row in enumerate(self.config):
      for x, piece in enumerate(row):
        if piece != '':
          square = self.squarepos((x,y))
          if piece[1] == 'R':
            square.occupying = Rook((x, y), 'white' if piece[0] == 'w' else 'black', self)
          # as you notice above, we put `self` as argument, or means our class Board
          elif piece[1] == 'N':
            square.occupying = Knight((x, y), 'white' if piece[0] == 'w' else 'black', self)
            
          elif piece[1] == 'B':
            square.occupying = Bishop((x, y), 'white' if piece[0] == 'w' else 'black', self)
            
          elif piece[1] == 'Q':
            square.occupying = Queen((x, y), 'white' if piece[0] == 'w' else 'black', self)
            
          elif piece[1] == 'K':
            square.occupying = King((x, y), 'white' if piece[0] == 'w' else 'black', self)
            
          elif piece[1] == 'P':
            square.occupying = Pawn((x, y), 'white' if piece[0] == 'w' else 'black', self)
            
  def handle_click(self, mx, my):
    x = mx // self.tilewidth
    y = my // self.tileheight
    clicked_square = self.squarepos((x,y))
    if self.selectedpiece is None:
      if clicked_square.occupying is not None:
        if clicked_square.occupying.colour == self.turn:
          self.selectedpiece = clicked_square.occupying 
          
    elif self.selectedpiece.move(self, clicked_square):
      if self.turn == 'black':
        self.turn = 'white'   
      else:
        self.turn = 'black'
        
    elif clicked_square.occupying is not None:
      if clicked_square.occupying.colour == self.turn:
        self.selectedpiece = clicked_square.occupying


  def is_in_check(self, colour, boardchange=None): #board_change = [(x1,y1), (x2,y2)]
    output = False
    kingpos = None
    
    changing_piece = None
    oldsquare = None
    newsquare = None
    newsquare_oldpiece = None
    
    if boardchange is not None:
      for square in self.squares:
        if square.pos == boardchange[0]:
          changing_piece = square.occupying
          oldsquare = square
          oldsquare.occupying = None
      for square in self.squares:
        if square.pos == boardchange[1]:
          newsquare = square
          newsquare_oldpiece = newsquare.occupying
          newsquare.occupying = changing_piece
          
    pieces = [
        i.occupying for i in self.squares if i.occupying is not None
    ]
    
    if changing_piece is not None:
      if changing_piece.notation == 'K':
        kingpos = newsquare.pos
    if kingpos == None:
        for piece in pieces:
          if piece.notation == 'K' and piece.colour == colour:
            kingpos = piece.pos
    for piece in pieces:
      if piece.colour != colour:
        for square in piece.attackingsquare(self):
          if square.pos == kingpos:
            output = True
    if boardchange is not None:
      oldsquare.occupying = changing_piece
      newsquare.occupying = newsquare_oldpiece
      
    return output


  def checkmate(self, colour):
    output = False
    
    for piece in [i.occupying for i in self.squares]:
      if piece != None:
        if piece.notation == 'K' and piece.colour == colour:
          king = piece
          
    if king.getvalidmove(self) == []:
      if self.is_in_check(colour):
        output = True
        
    return output

  def draw(self, display):
    if self.selectedpiece is not None:
      self.squarepos(self.selectedpiece.pos).highlight = True
      for square in  self.selectedpiece.getvalidmove(self):
        square.highlight = True
        
    for square in self.squares:
      square.draw(display)
      
      