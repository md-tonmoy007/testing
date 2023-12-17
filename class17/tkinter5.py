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

# colors = ['green', 'red', 'blue', 'orange', 'yellow', 'pink', 'purple',  'magenta', 'cyan']
# for i in colors:
#     random_rectangle(400, 400, i)

# canvas.create_arc(50, 10, 500, 300, extent=180, style=ARC)

imge = PhotoImage(file='tkinter.jpeg')
canvas.create_image(0, 0, anchor=NW, image=imge)


canvas.mainloop()