from  tkinter import *
import random
import time



tk =Tk()
tk.title("game")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)

canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
canvas.pack()
tk.update()


canvas.create_oval(10, 10, 25, 25, fill="red")



canvas.mainloop()