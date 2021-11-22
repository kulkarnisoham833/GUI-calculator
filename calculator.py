import tkinter as tk
import math
expression = ""


def press(num):
    global expression
    if num == "π":
        expression = expression + str(math.pi)
        equation.set(expression)
        return
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


# create gui
gui = tk.Tk()
gui.geometry("500x500")
# init buttons
button1 = tk.Button(gui, text="1", width=10, height=5,
                    bg="black", fg="white", command=lambda: press(1))
button1.grid(row=0, column=0)
button2 = tk.Button(gui, text="2", width=10, height=5,
                    bg="black", fg="white", command=lambda: press(2))
button2.grid(row=0, column=1)
button3 = tk.Button(gui, text="3", width=10, height=5,
                    bg="black", fg="white", command=lambda: press(3))
button3.grid(row=0, column=2)
button4 = tk.Button(gui, text="4", width=10, height=5,
                    bg="black", fg="white", command=lambda: press(4))
button4.grid(row=1, column=0)
button5 = tk.Button(gui, text="5", width=10, height=5,
                    bg="black", fg="white", command=lambda: press(5))
button5.grid(row=1, column=1)
button6 = tk.Button(gui, text="6", width=10, height=5,
                    bg="black", fg="white", command=lambda: press(6))
button6.grid(row=1, column=2)
button7 = tk.Button(gui, text="7", width=10, height=5,
                    bg="black", fg="white", command=lambda: press(7))
button7.grid(row=2, column=0)
button8 = tk.Button(gui, text="8", width=10, height=5,
                    bg="black", fg="white", command=lambda: press(8))
button8.grid(row=2, column=1)
button9 = tk.Button(gui, text="9", width=10, height=5,
                    bg="black", fg="white", command=lambda: press(9))
button9.grid(row=2, column=2)
button0 = tk.Button(gui, text="0", width=10, height=5,
                    bg="black", fg="white", command=lambda: press(0))
button0.grid(row=3, column=1)

buttonclear = tk.Button(gui, text="clear", width=10, height=5,
                        bg="black", fg="white", command=lambda: clear())
buttonclear.grid(row=3, column=0)

buttonequal = tk.Button(gui, text="=", width=10, height=5,
                        bg="black", fg="white", command=lambda: pressequal())
buttonequal.grid(row=3, column=2)

buttonplus = tk.Button(gui, text="+", width=10, height=5,
                       bg="black", fg="white", command=lambda: press("+"))
buttonplus.grid(row=0, column=4)

buttonminus = tk.Button(gui, text="-", width=10, height=5,
                        bg="black", fg="white", command=lambda: press("-"))
buttonminus.grid(row=1, column=4)

buttonmult = tk.Button(gui, text="*", width=10, height=5,
                       bg="black", fg="white", command=lambda: press("*"))
buttonmult.grid(row=2, column=4)

buttondiv = tk.Button(gui, text="/", width=10, height=5,
                      bg="black", fg="white", command=lambda: press("/"))
buttondiv.grid(row=3, column=4)
buttonpi = tk.Button(gui, text="π", width=10, height=5,
                     bg="black", fg="white", command=lambda: press("π"))
buttonpi.grid(row=0, column=5)
buttondecimal = tk.Button(gui, text=".", width=10, height=5,
                          bg="black", fg="white", command=lambda: press("."))
buttondecimal.grid(row=1, column=5)

equation = tk.StringVar()
expression_field = tk.Label(gui, textvariable=equation)
expression_field.grid(columnspan=4)

gui.mainloop()
