#  Create a Digitalclock

import tkinter as tk
from time import strftime

root = tk.Tk()
root.title("Digital Clock")

def time():
    string = strftime('%H:%M:%S %p\n\nMy Timer Machine\n\n%Y/%m/%d')
    label.config(text=string)
    label.after(1000, time)

label = tk.Label(root, font=('calibri', 50, 'bold'), background='yellow', foreground='black')
label.pack(anchor='center', padx=20, pady=20)

time()

root.mainloop()
