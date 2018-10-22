import calcView

from tkinter import *

if __name__ == "__main__":
    root = Tk()
    root.resizable(width=False, height=False)
    root.title("Calculator")
    app = calcView.CalcView(master=root)
    app.mainloop()
