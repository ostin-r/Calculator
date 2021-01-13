'''
Austin Richards 1/12/21 1744

This program will be the same calculator in calculator.py except with themes from 
RedFantom.  Might throw in some extra features as well.
'''

from tkinter import *
from tkinter import ttk as tk
from ttkthemes import ThemedTk

# initialize the themed window
gui = ThemedTk(theme='clearlooks')
gui.title('Simple Calculator')

# display
display = tk.Entry().grid(row=0, column=1)

# make the buttons
gen_width=4

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

but9.grid(row=1, column=2)
but8.grid(row=1, column=1)
but7.grid(row=1, column=0)

but6.grid(row=2, column=2)
but5.grid(row=2, column=1)
but4.grid(row=2, column=0)

but3.grid(row=3, column=2)
but2.grid(row=3, column=1)
but1.grid(row=3, column=0)

but0.grid(row=4, column=1)

# make the window go zoom
gui.mainloop()