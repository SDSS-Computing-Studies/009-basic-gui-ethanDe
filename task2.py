#python
#task2

import tkinter as tk
from tkinter import *
from tkinter import ttk

window = tk.Tk()
window.geometry("640x200")
window.configure(background='white')
window.title("T-Town Veterinary Clinic Database")
button1 = tk.Button(window,text="Search by Name", bg = "white",  borderwidth=1)
entrya = tk.Entry(window,text="Entry widgets can be typed in", borderwidth=1.5, relief=SUNKEN)
dogphoto = PhotoImage(file="dog.png")
labeld = tk.Label(window, image=dogphoto, borderwidth=0, relief=SUNKEN)
label1 = tk.Label(window,text="Client Database", bg = "white")

label2 = tk.Label(window,text="Name", bg = "white")
label3 = tk.Label(window,text="Type", bg = "white")
label4 = tk.Label(window,text="Breed", bg = "white")
label5 = tk.Label(window,text="Owner", bg = "white")
label6 = tk.Label(window,text="Birthdate", bg = "white")

entry1 = tk.Entry(window,text="Entry widgets can be typed in", borderwidth=3, relief=SUNKEN)
entry2 = tk.Entry(window,text="Entry widgets can be typed in", borderwidth=3, relief=SUNKEN)
entry3 = tk.Entry(window,text="Entry widgets can be typed in", borderwidth=3, relief=SUNKEN)
entry4 = tk.Entry(window,text="Entry widgets can be typed in", borderwidth=3, relief=SUNKEN)
entry5 = tk.Entry(window,text="Entry widgets can be typed in", borderwidth=3, relief=SUNKEN)

button2 = tk.Button(window,text="< Previous", bg = "white")
button3 = tk.Button(window,text="Save Entry", height = 2, width = 10)
button4 = tk.Button(window,text="Next >", bg = "white")

labeld.grid(row=0, column = 1, rowspan = 2)
label2.grid(row=3, column = 1)
entry1.grid(row=4, column = 1)
button2.grid(row = 5, column = 1, sticky = W)

label3.grid(row=3, column = 2)
entry2.grid(row=4, column = 2)

label1.grid(row=0, column = 3,rowspan = 2) #row1 rowspan 0
label4.grid(row=3, column = 3)
entry3.grid(row=4, column = 3)
button3.grid(row = 5, column = 3)

button1.grid(row=0, column = 4, sticky = E)
label5.grid(row=3, column = 4)
entry4.grid(row=4, column = 4)

entrya.grid(row=0, column = 5)
label6.grid(row=3, column = 5)
entry5.grid(row=4, column = 5)
button4.grid(row = 5, column = 5, sticky = E)

window.mainloop()