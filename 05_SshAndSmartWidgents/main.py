import tkinter as tk
import re

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)

        self.grid()
        self.t = tk.Text(self)
        self.t.grid()
        self.t.tag_config("wrong", background="red")
        self.tb = tk.Button(self, text="Обновить картинку по тексту", command=self.change_picture, font = 'Helvetica')
        self.tb.grid(row=1, column=0)


        self.c = tk.Canvas(self, bg='white')
        self.c.bind('<ButtonPress-1>', lambda event: self.create_oval_beg(event))
        self.c.bind('<ButtonRelease-1>', lambda event: self.create_oval_end(event))
        self.c.grid(row=0, column=1)
        self.cb = tk.Button(self, text="Обновить текст по картинке", command=self.change_text, font = 'Helvetica')
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
            self.c.create_oval(self.mouse_press[0], self.mouse_press[1], event.x, event.y, width = 7, outline = 'green', fill = 'limegreen')

    def change_text(self):
        self.t.delete('1.0', tk.END)
        for item in self.c.find_all():
            s = "oval: coords - " + str(", ".join(map(str, self.c.coords(item)))) + ", width - "+ str(self.c.itemcget(item, 'width')) + ", color - " + str(self.c.itemcget(item, 'outline')) + ", fill_color - "+ str(self.c.itemcget(item, 'fill')) + ".\n"
            self.t.insert(tk.END, s)

    def change_picture(self):
        s = self.t.get("1.0", tk.END).splitlines()
        self.t.tag_delete("wrong")
        self.c.delete("all")
        for i in range(len(s)):
            if s[i]:
                pattern = re.findall("oval: coords - (.*), (.*), (.*), (.*), width - (.*), color - (.*), fill_color - (.*).", s[i])
                if pattern != []:
                    coords = pattern[0][:4]
                    width = pattern[0][4]
                    color = pattern[0][5]
                    fill_color = pattern[0][6]
                    self.c.create_oval(*coords, width=width, outline=color, fill=fill_color)
                else:
                    self.t.tag_add("wrong", f"{i + 1}.0", f"{i + 1}.end")
        self.t.tag_config("wrong", background="red")
        

app = Application()
app.mainloop()
