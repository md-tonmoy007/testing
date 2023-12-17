import time
from tkinter import *

tk = Tk()

canvas = Canvas(tk, width=500, height=500)
canvas.pack()

canvas.create_rectangle(10, 10, 50, 50, fill="blue")

for i in range(0, 60):
    canvas.move(1, 5, 5)
    tk.update()
    time.sleep(0.05)

canvas.mainloop()

