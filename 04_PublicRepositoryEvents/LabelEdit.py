import tkinter as tk

class InputLabel(tk.Label):
    def __init__(self, master=None, text=""):
        tk.Label.__init__(self, master, text_=text, takefocus_=True, highlightthickness_=2, highlightcolor_='yellow',  borderwidth_=4, font_=("Monospace", 24), justify_='right', anchor_='w', relief = tk.GROOVE)
        self.text = text
        self.char_size = 15
        self.bind('<Any-KeyPress>', lambda event: self.letter_prod(event))
        self.bind('<Button-1>', lambda event: self.mouse_click(event))
        self.cursor_create()

    def letter_prod(self, event):
        if event.keycode == 22:
            if self.cursor_coord != 0:
                self["text"] = self["text"][:self.cursor_coord - 1] + self["text"][self.cursor_coord:]
                self.left_cursor_move()
        elif event.keysym == 'Right':
            self.right_cursor_move()
        elif event.keysym == 'Left':
            self.left_cursor_move()
        elif event.keysym == 'Home':
            self.cursor_coord = 0
        elif event.keysym == 'End':
            self.cursor_coord = len(self["text"])
        elif event.char.isalpha() or event.char.isdigit():
            self["text"] = self["text"][:self.cursor_coord] + event.char + self["text"][self.cursor_coord:]
            self.right_cursor_move()

        self.cursor_place()

    def cursor_create(self):
        self.cursor_coord = 0
        self.F = tk.Frame(self, borderwidth=5, background="red", height=30, width=2)
        self.cursor_place()

    def cursor_place(self):
        self.F.place(x=self.cursor_coord * self.char_size, y=0)

    def left_cursor_move(self):
        if self.cursor_coord >= 1:
            self.cursor_coord -= 1         

    def right_cursor_move(self):
        if self.cursor_coord < len(self["text"]):
            self.cursor_coord += 1
    
    def mouse_click(self, event):
        self.cursor_coord = event.x // self.char_size
        self.cursor_place()
        self.focus()

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()
        self.columnconfigure(0, weight=1)

    def createWidgets(self):
        self.L = InputLabel(self, text="")
        self.L.grid(row=1, column=0, sticky='NEWS')
        self.quitButton = tk.Button(self, text='Quit', command=self.quit)
        self.quitButton.grid(row=2, column=0, sticky='E')

app = Application()
app.mainloop()
