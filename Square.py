import pygame


class Square:
  def __init__(self,x,y,width,height):
    self.x = x #defines values in a class so i can use them 
    self.y = y
    self.width = width
    self.height = height
    
    self.absx = x * width # gets the absolute vaules of the squares for example 2*40=80
    self.absy = y * height # 1*40 = 40
    
    self.abspos = (self.absx,self.absy) #so coordinates of that square would be 80,40
    self.pos = (x,y)
    if ((x+y) % 2 == 0): #this is so everyother square is a diffrent colour 
      self.colour = 'light'
    else:
      self.colour = 'dark'
    if self.colour == 'light' : # this actually chooses the colour 
      self.drawcolour = (255, 255, 255)
    else :
      self.drawcolour = (0, 128, 0)
    if self.colour == 'light': # this is to hightlight where a pieces can go 
      self.highlight_colour = (100, 249, 83)
    else:
      self.highlight_colour = (0, 228, 10)
    self.occupying = None # checks if there is a piece on that square 
    self.coordinates = self.getcoordinates() #acesses the funtion getcoordinates to find the names of the squares
    self.highlight = False # all squares start witht the hightlight off
    self.rect = pygame.Rect(self.absx,self.absy,self.width,self.height) 
    #actually creates the square vaules 
    




  def getcoordinates(self):
    columns = 'abcdefgh'
    return columns[self.x] + str(self.y + 1)

  def draw(self,display):
    if self.highlight : 
      pygame.draw.rect(display, self.highlight_colour,self.rect)
    else:
      pygame.draw.rect(display, self.drawcolour,self.rect)
      #this draws the actual squares on the screen using all the data inputed
    
    if self.occupying != None: 
      centering_rect  = self.occupying.img.get_rect()
      centering_rect.center = self.rect.center
      display.blit(self.occupying.img, centering_rect.topleft)
"""this section checks if there is a pieces on it and if there is then gets picture and center it then draw the picture with the blit"""
