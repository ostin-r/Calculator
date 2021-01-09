'''
Austin Richards 1/5/21

this project made from the help of freeCodeCamp.org !!!
'''
from tkinter import *

gui = Tk()
gui.title("Simple Calculator")

# make the display
e = Entry(gui, width=35, borderwidth=2)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

# functions for the buttons
def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def clear_display():
    e.delete(0, END)

def button_add():
    first_number = e.get()
    global global_num
    global_num = int(first_number)
    e.delete(0, END)

def button_equal():
    second_number = e.get()
    e.delete(0, END)
    e.insert(0, global_num + int(second_number))


# make the buttons
but1 = Button(gui, text="1", padx=40, pady=20, command=lambda: button_click(1))
but2 = Button(gui, text="2", padx=40, pady=20, command=lambda: button_click(2))
but3 = Button(gui, text="3", padx=40, pady=20, command=lambda: button_click(3))
but4 = Button(gui, text="4", padx=40, pady=20, command=lambda: button_click(4))
but5 = Button(gui, text="5", padx=40, pady=20, command=lambda: button_click(5))
but6 = Button(gui, text="6", padx=40, pady=20, command=lambda: button_click(6))
but7 = Button(gui, text="7", padx=40, pady=20, command=lambda: button_click(7))
but8 = Button(gui, text="8", padx=40, pady=20, command=lambda: button_click(8))
but9 = Button(gui, text="9", padx=40, pady=20, command=lambda: button_click(9))
but0 = Button(gui, text="0", padx=40, pady=20, command=lambda: button_click(0))

but_add   = Button(gui, text="+", padx=39, pady=20, command=button_add)
but_equal = Button(gui, text="=", padx=39, pady=20, command=button_equal)
but_clear = Button(gui, text="clear", padx=130, pady=20, command=clear_display)

# put the buttons on the window
but1.grid(row=3, column=0)
but2.grid(row=3, column=1)
but3.grid(row=3, column=2)

but4.grid(row=2, column=0)
but5.grid(row=2, column=1)
but6.grid(row=2, column=2)

but7.grid(row=1, column=0)
but8.grid(row=1, column=1)
but9.grid(row=1, column=2)

but0.grid(row=4, column=1)

but_add.grid(row=4, column=0)
but_equal.grid(row=4, column=2)
but_clear.grid(row=5, column=0, columnspan=3)

gui.mainloop()