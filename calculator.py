'''
Austin Richards 1/2/21 16:21
'''
# making a window with tkinter
import tkinter as tk

class Window(tk.Frame):

    def __init__(self, master = None):
        tk.Frame.__init__(self, master)

        self.master = master

root = tk.Tk()

app = Window(root)

root.mainloop()