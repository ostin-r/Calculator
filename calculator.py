'''
Austin Richards 1/5/21

this project made from the help of freeCodeCamp.org !!!
'''

from tkinter import *
from tkinter import ttk

gui = Tk()
gui.title("Simple Calculator")

# make the display
e = Entry(gui, width=40, borderwidth=2)
e.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# create a style for the buttons
theme = 'default'
ttk.Style().theme_use(theme)

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
    global math
    math = "add"
    global_num = float(first_number)
    e.delete(0, END)

def button_sub():
    first_number = e.get()
    global global_num
    global math
    math = "sub"
    global_num = float(first_number)
    e.delete(0, END)

def button_mul():
    first_number = e.get()
    global global_num
    global math
    math = "mul"
    global_num = float(first_number)
    e.delete(0, END)

def button_div():
    first_number = e.get()
    global global_num
    global math
    math = "div"
    global_num = float(first_number)
    e.delete(0, END)

def button_equal():
    second_number = float(e.get())
    e.delete(0, END)

    if math == "add":
        e.insert(0, global_num + second_number)
    
    elif math == "sub":
        e.insert(0, global_num - second_number)

    elif math == "mul":
        e.insert(0, global_num * second_number)

    elif math == "div":
        if second_number == 0:
            e.insert(0, "divide by 0 error")
        else:
            e.insert(0, global_num/second_number)

    else:
        e.insert(0, 'error')

# make the buttons
gen_width = 10
gen_height = 3
but1 = Button(gui, text="1", width=gen_width, height=gen_height, command=lambda: button_click(1))
but2 = Button(gui, text="2", width=gen_width, height=gen_height, command=lambda: button_click(2))
but3 = Button(gui, text="3", width=gen_width, height=gen_height, command=lambda: button_click(3))
but4 = Button(gui, text="4", width=gen_width, height=gen_height, command=lambda: button_click(4))
but5 = Button(gui, text="5", width=gen_width, height=gen_height, command=lambda: button_click(5))
but6 = Button(gui, text="6", width=gen_width, height=gen_height, command=lambda: button_click(6))
but7 = Button(gui, text="7", width=gen_width, height=gen_height, command=lambda: button_click(7))
but8 = Button(gui, text="8", width=gen_width, height=gen_height, command=lambda: button_click(8))
but9 = Button(gui, text="9", width=gen_width, height=gen_height, command=lambda: button_click(9))
but0 = Button(gui, text="0", width=gen_width, height=gen_height, command=lambda: button_click(0))

but_equal = Button(gui, text="=", width=gen_width, height=gen_height, command=button_equal)
but_clear = Button(gui, text="clear", width= 44, height=gen_height, command=clear_display)

but_decimal = Button(gui, text=".", width=gen_width, height=gen_height, command=lambda: button_click("."))

but_add = Button(gui, text="+", width=gen_width, height=gen_height, command=button_add)
but_mul = Button(gui, text="*", width=gen_width, height=gen_height, command=button_mul)
but_div = Button(gui, text="/", width=gen_width, height=gen_height, command=button_div)
but_sub = Button(gui, text="-", width=gen_width, height=gen_height, command=button_sub)

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

but_add.grid(row=1, column=3)
but_sub.grid(row=2, column=3)
but_mul.grid(row=3, column=3)
but_div.grid(row=4, column=3)

but_equal.grid(row=4, column=2)
but_clear.grid(row=5, column=0, columnspan=4)

but_decimal.grid(row=4, column=0)

gui.mainloop()