'''
Austin Richards 1/12/21 1744

This program will be the same calculator in calculator.py except with themes from 
RedFantom's ttkthemes.  Might throw in some extra features as well.
'''

from tkinter import *
from tkinter import ttk as tk
from ttkthemes import ThemedTk

# initialize the themed window
gui = ThemedTk(theme='elegance')
gui.title('Simple Calculator')

# display
display = tk.Entry(width=30)
display.grid(row=0, column=0, columnspan=4, sticky="nesw")

# make the buttons
gen_width=10

but1 = tk.Button(gui, text='1', width=gen_width)
but2 = tk.Button(gui, text='2', width=gen_width)
but3 = tk.Button(gui, text='3', width=gen_width)
but4 = tk.Button(gui, text='4', width=gen_width)
but5 = tk.Button(gui, text='5', width=gen_width)
but6 = tk.Button(gui, text='6', width=gen_width)
but7 = tk.Button(gui, text='7', width=gen_width)
but8 = tk.Button(gui, text='8', width=gen_width)
but9 = tk.Button(gui, text='9', width=gen_width)
but0 = tk.Button(gui, text='0', width=gen_width)

but_add = tk.Button(gui, text='+', width=gen_width)
but_sub = tk.Button(gui, text='-', width=gen_width)
but_mul = tk.Button(gui, text='x', width=gen_width)
but_div = tk.Button(gui, text='/', width=gen_width)

but_decimal = tk.Button(gui, text='.', width=gen_width)
but_sign = tk.Button(gui, text='+/-', width=gen_width)
but_clear = tk.Button(gui, text='clear')
but_equal = tk.Button(gui, text='=')

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