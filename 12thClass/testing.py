
# https://realpython.com/python-gui-tkinter/
import tkinter as tk


window = tk.Tk()
window.geometry("500x500")

Label1 = tk.Label(window, text="Email", background="red", foreground="white")
Label1.grid(row=1, column=1)

email = tk.Text(window, fg="blue", bg="yellow", width=50, height=1)
email.grid(row=1, column=2)

Label2 = tk.Label(window, text="PassWord", background="red", foreground="white")
Label2.grid(row=2, column=1)

password = tk.Text(window, fg="blue", bg="yellow", width=50, height=1)
password.grid(row=2, column=2)


btn_1 = tk.Button(window, text="Submit", width=5)
btn_1.grid(row=3, column=2)



window.mainloop()
