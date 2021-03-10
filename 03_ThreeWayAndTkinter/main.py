import time
import tkinter as tk
from field import Field


class Application(tk.Tk):
    def __init__(self, field):
        self.field = field
        tk.Tk.__init__(self)
        self.columnconfigure(0, weight=1)
        self.buttonFrame = self.createButtonFrame()
        self.cellFrame = self.createButtonVidget()
        self.drawField()

    def createButtonFrame(self):
        F1 = tk.LabelFrame(self, relief = tk.GROOVE)
        F1.columnconfigure(0, weight=1)
        F1.grid(sticky='NEWS')
        N = tk.Button(F1, text = "New", command=self.new)
        N.grid(row=0, column=0, sticky='NEWS')
        E = tk.Button(F1, text = "Exit", command=self.quit)
        E.grid(row=0, column=1, sticky='NEWS')
        return F1

    def createButtonVidget(self):
        F2 = tk.LabelFrame(self, relief = tk.GROOVE)
        F2.columnconfigure(0, weight=1)
        F2.rowconfigure(0, weight=1)
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
            B = tk.Button(self.cellFrame, text=real_lab)
            B.grid(row=r, column=c, sticky='NEWS')
        self.cellFrame.grid(sticky='NEWS')


    def showtime(self):
        self.time.set(time.strftime("%c"))

    def createWidgets(self):
        self.time = tk.StringVar()
        self.timeButton = tk.Button(self, text='Time', command=self.showtime)
        self.quitButton = tk.Button(self, text='Quit', command=self.quit)
        self.timeLabel = tk.Label(self, textvariable=self.time)
        self.timeButton.grid()
        self.quitButton.grid(row=0, column=1)
        self.timeLabel.grid(columnspan=2)



f = Field()
app = Application(f)
app.mainloop()
