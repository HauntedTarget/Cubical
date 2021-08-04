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
    self.playerOffice.geometry('400x470')
    self.playerOffice.iconphoto(False, self.icon)
    self.poff = tkin.PhotoImage(file = 'Images/Office.png')
    self.frame = tkin.Frame(self.playerOffice)
    self.frame2 = tkin.Frame(self.playerOffice)
    self.frame3 = tkin.Frame(self.playerOffice)
    self.image = tkin.Label(self.frame, image = self.poff)
    self.button1 = tkin.Button(self.frame2, text='Use computer',command = self.computerOn)
    self.button2 = tkin.Button(self.frame2, text='Use File Cabanet',command = self.cabanetOpen)
    self.button3 = tkin.Button(self.frame3, text='Go To Hallway', command = self.poToHall)
    #Element packing
    self.image.pack(side='top')
    self.frame.pack(side='top')
    self.button1.pack(side='left')
    self.button2.pack(side='left')
    self.frame2.pack(side='top')
    self.button3.pack(side='top')
    self.frame3.pack(side='top')
  
  #Sends the player to the computer screen window
  def computerOn(self):
    self.playerOffice.destroy()
    self.coms()
  
  #Sends the player to the file cabanet(Store stuff from inventory to make space)
  def cabanetOpen(self):
    print('TEST')
  
  #Sends the player to the hall
  def poToHall(self):
    self.playerOffice.destroy()
    self.hall()
  
  def coms(self):
    #Element inits
    self.computer = tkin.Toplevel()
    self.computer.title('Cubical')
    self.computer.geometry('400x470')
    self.computer.iconphoto(False, self.icon)
    self.compng = tkin.PhotoImage(file = 'Images/Computer_V1.png')
    self.frame = tkin.Frame(self.computer)
    self.image = tkin.Label(self.frame, image = self.compng)
    #Element packing
    self.image.pack(side='top')
    self.frame.pack(side='top')

  def hall(self):
    #Element inits
    self.hallway = tkin.Toplevel()
    self.hallway.title('Cubical')
    self.hallway.geometry('400x470')
    self.hallway.iconphoto(False, self.icon)
    self.hallpic = tkin.PhotoImage(file = 'Images/Hallway.png')
    self.frame = tkin.Frame(self.hallway)
    self.image = tkin.Label(self.frame, image = self.hallpic)
    #Element packing
    self.image.pack(side='top')
    self.frame.pack(side='top')



#Makes the game start
gamestart = Game()