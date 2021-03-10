import time
import tkinter as tk
from field import Field
from tkinter import messagebox as mb

class Application(tk.Tk):
    def __init__(self, field):
        self.field = field
        tk.Tk.__init__(self)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        self.buttonFrame = self.createButtonFrame()
        self.cellFrame = self.createButtonVidget()
        self.drawField()

    def createButtonFrame(self):
        F1 = tk.LabelFrame(self, relief = tk.GROOVE)
        F1.grid()
        N = tk.Button(F1, text = "New", command=self.new)
        N.grid(row=0, column=0)
        E = tk.Button(F1, text = "Exit", command=self.quit)
        E.grid(row=0, column=1)
        return F1

    def createButtonVidget(self):
        F2 = tk.LabelFrame(self, relief = tk.GROOVE)
        for i in range(1, 5):
            F2.columnconfigure(i, weight=1)
            F2.rowconfigure(i, weight=1)
        F2.grid(sticky='NEWS')
        return F2

    def new(self):
        self.field.generateNew()
        self.drawField()

    def drawField(self):
        for (r, c), lab in self.field.get().items():
            real_lab = str(lab)
            if lab == 16:
                real_lab = ""
            B = tk.Button(self.cellFrame, text=real_lab, command= lambda x=(r,c): self.moveCell(x))
            B.grid(row=r, column=c, sticky='NEWS')
        self.cellFrame.grid(sticky='NEWS')

    def moveCell(self, c):
        self.field.move(c)
        self.drawField()
        if self.field.isWin():
            mb.showinfo("Поздравление", "Вы победили!")
            self.new()

f = Field()
app = Application(f)
app.mainloop()
