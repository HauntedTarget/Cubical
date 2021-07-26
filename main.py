#Imported Modules
import tkinter as tkin
import pickle
import random

#Varliables

#The initializer window
class Game:
  def __init__(self):
    #Initializes the main window
    self.start = tkin.Tk()
    self.start.title('Cubical')
    self.start.geometry("200x140")
    self.icon = tkin.PhotoImage(file = "Images/c.png")
    self.start.iconphoto(False, self.icon)
    self.menu = tkin.Frame(self.start)
    self.title = tkin.Label(self.menu,text='Cubicle\nA Game by Haunted Target')
    self.new = tkin.Button(self.menu,text='New Game',command = self.newGame)
    self.load = tkin.Button(self.menu,text='Continue',command = self.loadGame)
    self.quit = tkin.Button(self.menu,text='Quit',command = self.start.destroy)
    #Pack the label and buttons then the frame
    self.title.pack(side='top')
    self.new.pack(side='top')
    self.load.pack(side='top')
    self.quit.pack(side='top')
    self.menu.pack(side='top')

    tkin.mainloop()
    
  #New Game Command
  def newGame(self):
    self.start.withdraw()
    #Makes a random 8 digit seed
    random.seed(random.randint(10000000,100000000))
    self.office()
  
  #Loads the player game data
  def loadGame(self):
    print("TEST")
  
  #The player's office
  def office(self):
    #Element inits
    self.playerOffice = tkin.Toplevel()
    self.playerOffice.title('Cubical')
    self.playerOffice.geometry('400x450')
    self.playerOffice.iconphoto(False, self.icon)
    self.poff = tkin.PhotoImage(file = 'Images/Office.png')
    self.frame = tkin.Frame(self.playerOffice)
    self.image = tkin.Label(self.frame, image = self.poff)
    #Element packing
    self.image.pack(side='top')
    self.frame.pack(side='top')



#Makes the game work
gamestart = Game()