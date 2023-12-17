from tkinter import *

tk = Tk()

window = Canvas(tk, width = 720, height=500)
window.pack()

window.create_arc(100, 10, 50, 200, extent=180, style=ARC)


window.mainloop()