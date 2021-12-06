#python
#task2

import tkinter as tk
from tkinter import *
from tkinter import ttk

window = tk.Tk()
window.geometry("500x500")
window.title("T-Town Veterinary Clinic Database")
button1 = tk.Button(window,text="Search by Name")
entrya = tk.Entry(window,text="Entry widgets can be typed in", borderwidth=3, relief=SUNKEN)
dogphoto = PhotoImage(file="dog.png")
labeld = tk.Label(window, image=dogphoto, borderwidth=3, relief=SUNKEN)
label1 = tk.Label(window,text="Client Database")

label2 = tk.Label(window,text="Name")
label3 = tk.Label(window,text="Type")
label4 = tk.Label(window,text="Breed")
label5 = tk.Label(window,text="Owner")
label6 = tk.Label(window,text="Birthdate")

entry1 = tk.Entry(window,text="Entry widgets can be typed in", borderwidth=3, relief=SUNKEN)
entry2 = tk.Entry(window,text="Entry widgets can be typed in", borderwidth=3, relief=SUNKEN)
entry3 = tk.Entry(window,text="Entry widgets can be typed in", borderwidth=3, relief=SUNKEN)
entry4 = tk.Entry(window,text="Entry widgets can be typed in", borderwidth=3, relief=SUNKEN)
entry5 = tk.Entry(window,text="Entry widgets can be typed in", borderwidth=3, relief=SUNKEN)

button2 = tk.Button(window,text="< Previous")
button3 = tk.Button(window,text="Enter")
button4 = tk.Button(window,text="Next >")

labeld.grid(row=3, column = 1, columnspan=2)



window.mainloop()