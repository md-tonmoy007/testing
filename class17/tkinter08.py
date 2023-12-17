import time
from tkinter import *

tk = Tk()

def moveRect(event):
    canvas.move(1, 5, 0)


canvas = Canvas(tk, width=500, height=500)
canvas.pack()

canvas.create_rectangle(10, 10, 50, 50, fill="blue")

canvas.bind_all('<KeyPress-Return>', moveRect)

canvas.mainloop()