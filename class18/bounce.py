from tkinter import *
import random 
import time



class Ball:
    def __init__(self, window, color):
        self.window = window
        self.id = window.create_oval(10, 10, 25, 25, fill=color)
        self.window.move(self.id, 245, 100)
        starts = [-3, -2, -1, 1, 2, 3]
        random.shuffle(starts)
        self.x = starts[0] # -3 / -2 / -1 / .....
        self.y = -3
        self.canvas_height = self.window.winfo_height()
        self.canvas_width = self.window.winfo_width()


    def draw(self):
        self.window.move(self.id, self.x, self.y)
        pos = self.window.coords(self.id)
        print("pos: ", pos)
        if pos[1] <=0:
            self.y = 1

        if pos[0] <= 0:
            self.x = 1

        if pos[3] >= self.canvas_height:
            self.y = -1

        if pos[2] >= self.canvas_width:
            self.x = -1



tk = Tk()
tk.title("My first good animation")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
window = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
window.pack()

window.update() # animation run

ball = Ball(window, 'red')





while True:
    ball.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01) # freezes the code

tk.mainloop()