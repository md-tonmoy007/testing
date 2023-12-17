import time
from tkinter import *

tk = Tk()

def moveRect(event):
    if(event.keysym=="Up"):
        canvas.move(1, 0, -3)


canvas = Canvas(tk, width=500, height=500)
canvas.pack()

canvas.create_rectangle(10, 10, 50, 50, fill="blue")

canvas.bind_all('<KeyPress-Up>', moveRect)

canvas.mainloop()