from tkinter import *

tk = Tk()

window = Canvas(tk, width = 720, height=500)
window.pack()

# 
window.create_text(150, 100, text="My name is raisa", fill="red", font=("Courier", 30))


window.mainloop()