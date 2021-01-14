'''
Austin Richards 1/12/21 1744

This program will be the same calculator in calculator.py except with themes from 
RedFantom's ttkthemes.  Might throw in some extra features as well.
'''

from tkinter import *
from tkinter import ttk as tk
from ttkthemes import ThemedTk

# initialize the themed window
gui = ThemedTk(theme='clearlooks')
gui.title('Simple Calculator')

# display
display = tk.Entry(width=30)
display.grid(row=0, column=0, columnspan=4, sticky="nsew")

# functions for the buttons
def button_click(number):
    current = display.get()
    display.delete(0, END)
    display.insert(0, str(current) + str(number))

def clear_display():
    display.delete(0, END)

def sign_change():
    numb = display.get()
    display.delete(0, END)
    display.insert(0, "-" + str(numb))

def button_add():
    first_number = display.get()
    global global_num
    global math
    math = "add"
    global_num = float(first_number)
    display.delete(0, END)

def button_sub():
    first_number = display.get()
    global global_num
    global math
    math = "sub"
    global_num = float(first_number)
    display.delete(0, END)

def button_mul():
    first_number = display.get()
    global global_num
    global math
    math = "mul"
    global_num = float(first_number)
    display.delete(0, END)

def button_div():
    first_number = display.get()
    global global_num
    global math
    math = "div"
    global_num = float(first_number)
    display.delete(0, END)

def button_equal():
    second_number = float(display.get())
    display.delete(0, END)

    if math == "add":
        display.insert(0, global_num + second_number)
    
    elif math == "sub":
        display.insert(0, global_num - second_number)

    elif math == "mul":
        display.insert(0, global_num * second_number)

    elif math == "div":
        if second_number == 0:
            display.insert(0, "divide by 0 error")
        else:
            display.insert(0, global_num/second_number)

    else:
        display.insert(0, 'error')

# make the buttons
gen_width=6

but1 = tk.Button(gui, text='1', width=gen_width, command=lambda: button_click(1))
but2 = tk.Button(gui, text='2', width=gen_width, command=lambda: button_click(2))
but3 = tk.Button(gui, text='3', width=gen_width, command=lambda: button_click(3))
but4 = tk.Button(gui, text='4', width=gen_width, command=lambda: button_click(4))
but5 = tk.Button(gui, text='5', width=gen_width, command=lambda: button_click(5))
but6 = tk.Button(gui, text='6', width=gen_width, command=lambda: button_click(6))
but7 = tk.Button(gui, text='7', width=gen_width, command=lambda: button_click(7))
but8 = tk.Button(gui, text='8', width=gen_width, command=lambda: button_click(8))
but9 = tk.Button(gui, text='9', width=gen_width, command=lambda: button_click(9))
but0 = tk.Button(gui, text='0', width=gen_width, command=lambda: button_click(0))

but_add = tk.Button(gui, text='+', width=gen_width, command=button_add)
but_sub = tk.Button(gui, text='-', width=gen_width, command=button_sub)
but_mul = tk.Button(gui, text='x', width=gen_width, command=button_mul)
but_div = tk.Button(gui, text='/', width=gen_width, command=button_div)

but_decimal = tk.Button(gui, text='.', width=gen_width, command=lambda: button_click("."))
but_sign    = tk.Button(gui, text='+/-', width=gen_width, command=sign_change)
but_clear   = tk.Button(gui, text='clear', command=clear_display)
but_equal   = tk.Button(gui, text='=', command=button_equal)

# put the buttons in the window
but9.grid(row=1, column=2)
but8.grid(row=1, column=1)
but7.grid(row=1, column=0)

but6.grid(row=2, column=2)
but5.grid(row=2, column=1)
but4.grid(row=2, column=0)

but3.grid(row=3, column=2)
but2.grid(row=3, column=1)
but1.grid(row=3, column=0)

but_sign.grid(row=4, column=0)
but0.grid(row=4, column=1)
but_decimal.grid(row=4, column=2)

but_add.grid(row=1, column=3)
but_sub.grid(row=2, column=3)
but_mul.grid(row=3, column=3)
but_div.grid(row=4, column=3)

but_clear.grid(row=5, column=0, columnspan=2, sticky="nesw")
but_equal.grid(row=5, column=2, columnspan=2, sticky="nesw")

# make the window go zoom
gui.mainloop()