from  tkinter import *
import random

def random_rectangle(width, height, f_color):
    x1 = random.randrange(width)
    y1 = random.randrange(height)
    x2 = x1 + random.randrange(width)
    y2 = y1 + random.randrange(height)
    canvas.create_rectangle(x1, y1, x2, y2, fill=f_color)


tk = Tk()
canvas = Canvas(tk, width=500, height=500)
canvas.pack()
colors = ['green', 'red', 'blue', 'orange', 'yellow', 'pink', 'purple',  'magenta', 'cyan']
# random_rectangle(400, 400, "red")
# random_rectangle(300, 300, "blue")
for color in  colors:
    random_rectangle(400, 400, color)


canvas.mainloop()