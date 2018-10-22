from tkinter import *
from tkinter.ttk import *

class GridFrame(Frame):

    def __init__(self, buttons, view, xsize, ysize, fg, bg, master=None):
        Frame.__init__(self,master)
        self.buttonNames = buttons
        self.dimensions = (xsize, ysize)
        self.background = fg
        self.foreground = bg
        self.view = view

    def addButton(self, num):
        text = self.buttonNames[num]
        command = lambda : self.view.handleInput(text)
        self.button = Button(self, text = text, command = command)

        x = num % self.dimensions[0]
        y = num // self.dimensions[0]

        if(y >= self.dimensions[1]):
            return

        self.button.grid(row = (y), column = (x))

    def construct(self):

        Style().configure("TButton", padding=(0, 5, 0, 5), 
            font='courier',background=self.background,
                          foreground=self.foreground)
        
        for x in range(0, self.dimensions[0]):
            self.columnconfigure(x, weight = 1)
        for y in range(0, self.dimensions[1]):
            self.rowconfigure(y, weight = 1)

        for i in range(0, len(self.buttonNames)):
            self.addButton(i);

        

        

        
        
