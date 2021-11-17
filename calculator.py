import tkinter as tk
expression = ""


def press(num):
    global expression
    expression = expression + str(num)

    # update the expression by using set method
    equation.set(expression)


def clear():
    global expression
    expression = ""
    equation.set("")


def pressequal():
    global expression
    try:
        total = str(eval(expression))
    except(SyntaxError):
        total = str(eval(expression))
    expression = str(total)
    equation.set(total)


gui = tk.Tk()
gui.geometry("500x500")
button1 = tk.Button(gui, text="1", width=10, height=5,
                    bg="black", fg="white", command=lambda: press(1), font=tk.font.Font(size=16))
button1.grid(row=0, column=0)
button2 = tk.Button(gui, text="2", width=10, height=5,
                    bg="black", fg="white", command=lambda: press(2), font=tk.font.Font(size=16))
button2.grid(row=0, column=1)
button3 = tk.Button(gui, text="3", width=10, height=5,
                    bg="black", fg="white", command=lambda: press(3), font=tk.font.Font(size=16))
button3.grid(row=0, column=2)
button4 = tk.Button(gui, text="4", width=10, height=5,
                    bg="black", fg="white", command=lambda: press(4), font=tk.font.Font(size=16))
button4.grid(row=1, column=0)
button5 = tk.Button(gui, text="5", width=10, height=5,
                    bg="black", fg="white", command=lambda: press(5), font=tk.font.Font(size=16))
button5.grid(row=1, column=1)
button6 = tk.Button(gui, text="6", width=10, height=5,
                    bg="black", fg="white", command=lambda: press(6), font=tk.font.Font(size=16))
button6.grid(row=1, column=2)
button7 = tk.Button(gui, text="7", width=10, height=5,
                    bg="black", fg="white", command=lambda: press(7), font=tk.font.Font(size=16))
button7.grid(row=2, column=0)
button8 = tk.Button(gui, text="8", width=10, height=5,
                    bg="black", fg="white", command=lambda: press(8), font=tk.font.Font(size=16))
button8.grid(row=2, column=1)
button9 = tk.Button(gui, text="9", width=10, height=5,
                    bg="black", fg="white", command=lambda: press(9), font=tk.font.Font(size=16))
button9.grid(row=2, column=2)
button0 = tk.Button(gui, text="0", width=10, height=5,
                    bg="black", fg="white", command=lambda: press(0), font=tk.font.Font(size=16))
button0.grid(row=3, column=1)

buttonclear = tk.Button(gui, text="clear", width=10, height=5,
                        bg="black", fg="white", command=lambda: clear(), font=tk.font.Font(size=16))
buttonclear.grid(row=3, column=0)

buttonequal = tk.Button(gui, text="=", width=10, height=5,
                        bg="black", fg="white", command=lambda: pressequal(), font=tk.font.Font(size=16))
buttonequal.grid(row=3, column=2)

buttonplus = tk.Button(gui, text="+", width=10, height=5,
                       bg="black", fg="white", command=lambda: press("+"), font=tk.font.Font(size=16))
buttonplus.grid(row=0, column=4)

buttonminus = tk.Button(gui, text="-", width=10, height=5,
                        bg="black", fg="white", command=lambda: press("-"), font=tk.font.Font(size=16))
buttonminus.grid(row=1, column=4)

buttonmult = tk.Button(gui, text="*", width=10, height=5,
                       bg="black", fg="white", command=lambda: press("*"), font=tk.font.Font(size=16))
buttonmult.grid(row=2, column=4)

buttondiv = tk.Button(gui, text="/", width=10, height=5,
                      bg="black", fg="white", command=lambda: press("/"), font=tk.font.Font(size=16))
buttondiv.grid(row=3, column=4)

equation = tk.StringVar()
expression_field = tk.Label(gui, textvariable=equation)
expression_field.grid(columnspan=4)

gui.mainloop()
