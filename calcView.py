import calcController
import gridPanel

from tkinter import *



class CalcView(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)

        self.controller = calcController.CalcController()

        self.label = Label(self, bg="green", fg="white", font=("Courier", 16), height=1)

        self.label.pack(fill = X)


        self.buttonFrame = Frame(self)
        
        self.numPanel = self.getNumPanel()
        self.numPanel.construct()
        self.numPanel.grid(row=0, column=0)

        self.opPanel = self.getOperationPanel()
        self.opPanel.construct()
        self.opPanel.grid(row=0, column=1)


        self.buttonFrame.pack(fill = X)
        self.pack()
        

    def handleInput(self, text):
        self.label["text"] = self.controller.handleInput(text)

    def getNumPanel(self):
        numPanelButtons = ["1","2","3","4","5","6","7","8","9","0","(",")"]
        return gridPanel.GridFrame(numPanelButtons,self,3,4,
                                   "red","blue",master=self.buttonFrame)

    def getOperationPanel(self):
        operationButtons = ["AC","DEL","+","-","*","/",".","="]
        return gridPanel.GridFrame(operationButtons,self,2,4,
                                   "red","blue",master=self.buttonFrame)



