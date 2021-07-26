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
    self.seedChoose()
  
  def loadGame(self):
    print("TEST")
  
  def seedChoose(self):
    #The window that asks for the user to type a seed or play a random one
    self.seedWindow = tkin.Toplevel()
    self.start.title('Cubical')
    self.seedWindow.geometry('200x90')
    self.seedWindow.iconphoto(False, self.icon)
    self.box = tkin.Frame(self.seedWindow)
    self.seed = tkin.Entry(self.box)
    self.seed.insert(0,'Set Seed')
    self.useSeed = tkin.Button(self.box,text='Use Seed',command=self.seedStart)
    self.randomSeed = tkin.Button(self.box,text='Random Seed',command=self.randomStart)
    #Packs the window
    self.seed.pack(side='top')
    self.useSeed.pack(side='top')
    self.randomSeed.pack(side='top')
    self.box.pack(side='top')

  def seedStart(self):
    try:
      seed = int(self.seed.get())
      random.seed(seed)
    except:
      random.seed(random.randint(10000000,100000000))
    self.seedWindow.destroy()
    print('TEST')
  
  def randomStart(self):
    print('TEST')


#Makes the game work
gamestart = Game()