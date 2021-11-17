import tkinter as tk
expression = ""


def buttonpress(num):
    global expression
    expression += str(num)


def calculate():  # note that calculate should be called after some buttonpress()'s, since it's pretty much an equal sign
    global expression
    total = eval(expression)
    print(total)


# init gui
gui = tk.Tk()
gui.title("Calculator")
gui.geometry("300x300")
gui.configure(background="black")
# Create buttons
button_1 = tk.Button(gui, text="1", fg="white", bg="black",
                     command=buttonpress(1), width=3, height=1)
button_2 = tk.Button(gui, text="2", fg="white", bg="black",
                     command=buttonpress(2), width=3, height=1)
button_3 = tk.Button(gui, text="3", fg="white", bg="black",
                     command=buttonpress(3), width=3, height=1)
button_4 = tk.Button(gui, text="4", fg="white", bg="black",
                     command=buttonpress(4), width=3, height=1)
button_5 = tk.Button(gui, text="5", fg="white", bg="black",
                     command=buttonpress(5), width=3, height=1)
button_6 = tk.Button(gui, text="6", fg="white", bg="black",
                     command=buttonpress(6), width=3, height=1)
button_7 = tk.Button(gui, text="7", fg="white", bg="black",
                     command=buttonpress(7), width=3, height=1)
button_8 = tk.Button(gui, text="8", fg="white", bg="black",
                     command=buttonpress(8), width=3, height=1)
button_9 = tk.Button(gui, text="9", fg="white", bg="black",
                     command=buttonpress(9), width=3, height=1)
button_0 = tk.Button(gui, text="0", fg="white", bg="black",
                     command=buttonpress(0), width=3, height=1)
button_add = tk.Button(gui, text="+", fg="white", bg="black",
                       command=buttonpress("+"), width=3, height=1)
button_sub = tk.Button(gui, text="-", fg="white", bg="black",
                       command=buttonpress("-"), width=3, height=1)
button_mul = tk.Button(gui, text="*", fg="white", bg="black",
                       command=buttonpress("*"), width=3, height=1)
button_div = tk.Button(gui, text="/", fg="white", bg="black",
                       command=buttonpress("/"), width=3, height=1)
button_equal = tk.Button(gui, text="=", fg="white",
                         bg="black", command=calculate(), width=3, height=1)
button_clear = tk.Button(gui, text="C", fg="white",
                         bg="black", width=3, height=1)
