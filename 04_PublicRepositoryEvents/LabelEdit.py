import tkinter as tk

class InputLabel(tk.Label):
    def __init__(self, master=None, text=""):
        tk.Label.__init__(self, master, text_=text, takefocus_=True, highlightthickness_=2, highlightcolor_ = 'yellow')
        self.text = text

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        self.L = InputLabel(self, text="Lower letters only")
        self.L.grid(row=1, column=0)
        self.L.bind('<Any-KeyPress>', lambda event: self.letter_prod(event))
        #self.master.bind('<Any-KeyPress>', lambda event: print("Root", event))
        #self.L1 = tk.Label(self, text="Lower letters only", takefocus=True, highlightthickness=2, highlightcolor = 'red')
        #self.L1.grid(row=1, column=3)
        #self.L1.bind('<Any-KeyPress>', lambda event: print("L1", event))
        self.quitButton = tk.Button(self, text='Quit', command=self.quit)
        self.quitButton.grid(row=1, column=1)
   
    def letter_prod(self, event):
        if event.keycode == 22:
            self.L["text"] = self.L["text"][:-1]
        elif event.char.isalpha() or event.char.isdigit():
            self.L["text"] += str(event.char)

app = Application()
app.mainloop()
