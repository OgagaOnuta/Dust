#!/usr/bin/python3

'''
Ttk widget names: TButton, TCheckbutton, TCombobox, TEntry, TFrame,
TLabel, TLabelframe, TMenubutton, TNotebook, TProgressbar,
TRadiobutton, TScale, TScrollbar, TSpinbox, Treeview
'''

from tkinter import *
from tkinter import messagebox
from tkinter import ttk


def open_msg_box():
    messagebox.showwarning(
        "Event Triggered",
        "Button Clicked"
    )


root = Tk()

root.geometry("400x400+300+300")
root.resizable(width=False, height=False)

frame = Frame(root)

style = ttk.Style()

style.configure("TButton",
                foreground="midnight blue",
                font="Times 20 bold italic",
                padding=20)

print(ttk.Style().theme_names())
print(style.lookup("TButton", "font"))
print(style.lookup("TButton", "foreground"))
print(style.lookup("TButton", "padding"))

ttk.Style().theme_use("classic")

theButton = ttk.Button(frame,
                       text="Important Button",
                       command=open_msg_box)

theButton["state"] = "disabled"
theButton["state"] = "normal"

theButton.pack()
frame.pack()

root.mainloop()
