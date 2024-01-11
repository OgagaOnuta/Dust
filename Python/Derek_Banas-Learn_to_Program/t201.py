#!/usr/bin/python3

from tkinter import *
from tkinter import ttk

root = Tk()

# A frame is a widget that surrounds other widgets
frame = Frame(root)

labelText = StringVar()

label = Label(frame, textvariable=labelText)
button = Button(frame, text="Click Me")

labelText.set("I am a label")

label.pack()
button.pack()
frame.pack()

root.mainloop()
