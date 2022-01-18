
#python
#task4

import tkinter as tk
from tkinter import *
from tkinter import ttk

window = tk.Tk()
window.title("Example")
window.geometry("260x150")
window.configure(bg= "white")
dogphoto = PhotoImage(file="dog.png")
labeld = tk.Label(window, image=dogphoto, borderwidth=0, relief=SUNKEN)
labelm = tk.Label(window,text="A cuddly little puppy! This is from the same \n creators who brought you Keropi and Kero Kero", bg = "#A3FFFF")
labels = tk.Label(window,text="Pochacco!", bg = "white")

labeld.place(relx = 0.4, rely = 0.4, anchor = CENTER)
labels.place(relx = 0.65, rely = 0.4, anchor = CENTER)
labelm.place(relx = 0.5, rely = 0.88, anchor = CENTER)

window.mainloop()