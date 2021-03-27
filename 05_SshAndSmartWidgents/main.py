import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)

        self.grid()
        self.t = tk.Text(self)
        self.t.grid()
        self.tb = tk.Button(self, text="Обновить картинку по тексту")
        self.tb.grid(row=1, column=0)

        self.c = tk.Canvas(self, bg='white')
        self.c.bind('<ButtonPress-1>', lambda event: self.create_oval_beg(event))
        self.c.bind('<ButtonRelease-1>', lambda event: self.create_oval_end(event))
        self.c.grid(row=0, column=1)
        self.cb = tk.Button(self, text="Обновить текст по картинке", command=self.change_text)
        self.cb.grid(row=1, column=1)


    def create_oval_beg(self, event):
        item = self.c.find_withtag(tk.CURRENT)
        self.mouse_press = event.x, event.y
        if item:
            self.exist_flag = True
            self.item = item
        else:
            self.exist_flag = False
            self.item = None

    def create_oval_end(self, event):
        if self.exist_flag:
            self.c.move(self.item, event.x - self.mouse_press[0], event.y - self.mouse_press[1])
        else:
            self.c.create_oval(self.mouse_press[0], self.mouse_press[1], event.x, event.y, width = 7, outline = 'green')

    def change_text(self):
        self.t.delete('1.0', tk.END)
        for item in self.c.find_all():
            s = str(self.c.coords(item)) + str(self.c.itemcget(item, 'width')) + str(self.c.itemcget(item, 'outline'))
            self.t.insert(tk.END, s)

app = Application()
app.mainloop()
