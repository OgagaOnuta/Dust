#!/usr/bin/python3

'''
------------------------- MULTIPLE COMPONENTS -------------------------
Some of the different Widgets: Button, Label, Canvas, Menu, Text, Scale,
OptionMenu, Frame, CheckButton, LabelFrame, MenuButton, PanedWindow, Entry,
ListBox, Message, RadioButton, ScrollBar, Bitmap, SpinBox, Image
'''

from tkinter import *
from tkinter import ttk
# import tkinter

# tkinter._test()

# Tk object representing the main window
root = Tk()

root.title("First GUI")
ttk.Button(root, text="Hello TkInter").grid()

root.mainloop()
