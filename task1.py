#python
#task 1

import tkinter as tk
from tkinter import *
from tkinter import ttk

window = tk.Tk()
window.title("tk")


entry1 = tk.Entry(window,text="Entry widgets can be typed in", borderwidth=1, width = 15, relief=SUNKEN)
label1 = tk.Label(window,text=" x ", borderwidth=1, bg = "white")
entry2 = tk.Entry(window,text="Entry widgets can be typed in", borderwidth=1, width = 15, relief=SUNKEN)
button1 = tk.Button(window,text="=", borderwidth=1, bg = "white")
entry3 = tk.Entry(window,text="Entry widgets can be typed in", borderwidth=1, width = 22, relief=SUNKEN)

entry1.pack(side=LEFT)
label1.pack(side=LEFT)
entry2.pack(side=LEFT)
button1.pack(side=LEFT)
entry3.pack(side=LEFT)

window.mainloop()