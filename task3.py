#python
#task3

import tkinter as tk
from tkinter import *
from tkinter import ttk

window = tk.Tk()
window.title("Example")
window.configure(bg= "white")
dogphoto = PhotoImage(file="dog.png")
labeld = tk.Label(window, image=dogphoto, borderwidth=0, relief=SUNKEN)
labelm = tk.Label(window,text="A cuddly little puppy! This is from the same \n creators who brought you Keropi and Kero Kero", bg = "#A3FFFF")
labels = tk.Label(window,text="Pochacco!", bg = "white")

labeld.grid(row=0, column = 0, sticky = E)
labels.grid(row=0, column = 1, sticky = W)
labelm.grid(row=1, column = 0, columnspan = 2)

window.mainloop()