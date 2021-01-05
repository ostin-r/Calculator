'''
Austin Richards 1/4/21 16:35
'''

from tkinter import *

root = Tk()

# set the window size
root.geometry("347x330")

# print whatever the user clicks on the top of the calculator
def print_data():
    # figure out how to do this part

# make the required buttons for the calculator
but0 = Button(root, text="0", height=50)
but1 = Button(root, text="1")
but2 = Button(root, text="2")
but3 = Button(root, text="3")
but4 = Button(root, text="4")
but5 = Button(root, text="5")
but6 = Button(root, text="6")
but7 = Button(root, text="7")
but8 = Button(root, text="8")
but9 = Button(root, text="9")

but_add = Button(root, text="+")
but_sub = Button(root, text="-")
but_mul = Button(root, text="*")
but_div = Button(root, text="/")

but_sig = Button(root, text="(+/-)")
but_dec = Button(root, text=".")

# put the buttons in the window, this can probably be done with a loop
but1.grid(row=1, column=0)
but2.grid(row=1, column=1)
but3.grid(row=1, column=2)
but4.grid(row=2, column=0)
but5.grid(row=2, column=1)
but6.grid(row=2, column=2)
but7.grid(row=3, column=0)
but8.grid(row=3, column=1)
but9.grid(row=3, column=2)
but0.grid(row=4, column=1)

but_add.grid(row=1, column=3)
but_sub.grid(row=2, column=3)
but_mul.grid(row=3, column=3)
but_div.grid(row=4, column=3)

but_sig.grid(row=4, column=0)
but_dec.grid(row=4, column=2)

# set button size
h = 4
w = 11

but1.config(height=h, width=w)
but2.config(height=h, width=w)
but3.config(height=h, width=w)
but4.config(height=h, width=w)
but5.config(height=h, width=w)
but6.config(height=h, width=w)
but7.config(height=h, width=w)
but8.config(height=h, width=w)
but9.config(height=h, width=w)
but0.config(height=h, width=w)

but_add.config(height=h, width=w)
but_sub.config(height=h, width=w)
but_mul.config(height=h, width=w)
but_div.config(height=h, width=w)

but_sig.config(height=h, width=w)
but_dec.config(height=h, width=w)

# now for the fun part. Make the buttons do shit.


root.mainloop()