'''
Austin Richards 1/2/21 16:21
'''
# making a window with tkinter
from tkinter import *

root = Tk()

entry = Entry(root, width=15, borderwidth=3)
entry.pack()
entry.insert(0, 'Enter your name')

def click_do():
    label = Label(root, text='Hello, ' + entry.get())
    label.pack()

first_button = Button(root, text='Enter', command=click_do)
first_button.pack()

root.mainloop()