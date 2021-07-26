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
    random.seed(random.randint(10000000,100000000))
    self.office()
  
  def loadGame(self):
    print("TEST")
  
  def office(self):
    print('TEST')


#Makes the game work
gamestart = Game()