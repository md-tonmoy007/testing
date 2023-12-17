import tkinter as tk

calculation = ""
num2 = 0
num1 =0
sym = ""

root = tk.Tk()
root.geometry("300x300")
txt = tk.Text(root, height=2, width=16)
txt.grid(columnspan=10)

def add_to_calc(number):
    global calculation
    calculation += str(number)
    txt.delete(1.0, "end")
    txt.insert(1.0, calculation)

def add_to_symbo(symbol):
    global calculation, sym, num1
    sym = symbol
    print("num1", num1, calculation)
    num1 = int(calculation)
    print("num1", num1)
    txt.delete(1.0, "end")
    calculation = ""

def evaluate_calculation():
    global calculation, sym, num1, num2
    print(calculation)
    num2 = int(calculation)
    txt.delete(1.0, "end")
    calculation = ""

    if (sym == "+"):
        result = num1 + num2
    elif(sym == "-"):
        result = num1 - num2
    elif(sym == "*"):
        result = num1 * num2
    elif(sym == "/"):
        result = num1 / num2
    else: 
        result = "Wrong operation"

    result = str(result)
    txt.insert(1.0, result)
    sym = ""

def clear():
    global calculation
    calculation = ""
    txt.delete(1.0, "end")


btn_1 = tk.Button(root, text="1", command=lambda:add_to_calc(1), width=5)
btn_1.grid(row=2, column=1)
btn_2 = tk.Button(root, text="2", command=lambda:add_to_calc(2), width=5)
btn_2.grid(row=2, column=2)
btn_3 = tk.Button(root, text="3", command=lambda:add_to_calc(3), width=5)
btn_3.grid(row=2, column=3)
btn_4 = tk.Button(root, text="4", command=lambda:add_to_calc(4), width=5)
btn_4.grid(row=3, column=1)
btn_5 = tk.Button(root, text="5", command=lambda:add_to_calc(5), width=5)
btn_5.grid(row=3, column=2)
btn_6 = tk.Button(root, text="6", command=lambda:add_to_calc(6), width=5)
btn_6.grid(row=3, column=3)
btn_7 = tk.Button(root, text="7", command=lambda:add_to_calc(7), width=5)
btn_7.grid(row=4, column=1)
btn_8 = tk.Button(root, text="8", command=lambda:add_to_calc(8), width=5)
btn_8.grid(row=4, column=2)
btn_9 = tk.Button(root, text="9", command=lambda:add_to_calc(9), width=5)
btn_9.grid(row=4, column=3)
btn_0 = tk.Button(root, text="0", command=lambda:add_to_calc(0), width=5)
btn_0.grid(row=5, column=2)

btn_plus = tk.Button(root, text="+", command=lambda:add_to_symbo("+"), width=5)
btn_plus.grid(row=2, column=4)
btn_min = tk.Button(root, text="-", command=lambda:add_to_symbo("-"), width=5)
btn_min.grid(row=3, column=4)
btn_mult = tk.Button(root, text="*", command=lambda:add_to_symbo("*"), width=5)
btn_mult.grid(row=4, column=4)
btn_div = tk.Button(root, text="/", command=lambda:add_to_symbo("/"), width=5)
btn_div.grid(row=5, column=4)


btn_equal = tk.Button(root, text="=", command=evaluate_calculation, width=5)
btn_equal.grid(row=5, column=1)
btn_clear = tk.Button(root, text="AC", command=clear, width=5)
btn_clear.grid(row=5, column=3)

root.mainloop()