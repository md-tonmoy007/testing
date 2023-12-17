from tkinter import *

tk = Tk()

window = Canvas(tk, width = 720, height=500)
window.pack()

# window.create_arc(100, 10, 50, 200, extent=180, style=ARC)
img = PhotoImage(file="1.jpg")
window.create_image(0, 0, anchor=NW, image=img)

window.mainloop()