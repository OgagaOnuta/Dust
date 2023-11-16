#!/usr/bin/python3

'''
Use Case Description
====================

At least 3 functions needed

  I. User clicks a number button (self, number)
       N3. With each number button pressed, add the new value to the end of the
           first and update the entry
 II. User clicks a math button (self, math_func)
       N1. Make sure entry has a value
       N2. Switch boolean values representing math buttons to false on entry
       N2. Have button pass in the math function pressed
       N4. Store the entry value on entry to this function (Class Field)
       N4. Clear the entry field
III. User clicks another number button
 IV. User clicks equal button and the result shows
       N1. Make sure a math function was clicked
       N2. Check which math function was clicked and provide d correct solution

Potential Problems
==================

Note 1: Make sure previous required button was clicked
Note 2: Make a way to track which math button was clicked last
Note 3: Think about a way to handle the user entering both single and multiple
        numbers
Note 4: Track the first number in the entry box after a math button is clicked
Note 5: What about division problems caused by an integer division?
     a. Convert to a float each time we retrieve or store values in the entry
'''

from tkinter import *
from tkinter import ttk


class Calculator:
    calc_value = 0.0

    div_trigger = False
    mult_trigger = False
    add_trigger = False
    sub_trigger = False

    def button_press(self, value):
        entry_val = self.number_entry.get()
        entry_val += value

        self.number_entry.delete(0, "end")
        self.number_entry.insert(0, entry_val)

    def isfloat(self, str_val):
        try:
            float(str_val)
            return (True)
        except (ValueError):
            return (False)

    def math_button_press(self, value):
        if self.isfloat(str(self.number_entry.get())):
            div_trigger = False
            mult_trigger = False
            add_trigger = False
            sub_trigger = False

            self.calc_value = float(self.entry_value.get())

            if (value == "/"):
                print("/ Pressed")
                self.div_trigger = True
            elif (value == "*"):
                print("* Pressed")
                self.mult_trigger = True
            elif (value == "+"):
                print("+ Pressed")
                self.add_trigger = True
            elif (value == "-"):
                print("- Pressed")
                self.sub_trigger = True

            self.number_entry.delete(0, "end")

    # FIND BUG IN FUNCTION
    def equal_button_press(self):
        if (
                self.div_trigger or self.mult_trigger or
                self.add_trigger or self.sub_trigger
        ):

            if (self.div_trigger):
                solution = self.calc_value / float(self.entry_value.get())
            elif (self.mult_trigger):
                solution = self.calc_value * float(self.entry_value.get())
            elif (self.add_trigger):
                solution = self.calc_value + float(self.entry_value.get())
            elif (self.sub_trigger):
                solution = self.calc_value - float(self.entry_value.get())

            print(self.calc_value, " ",
                  float(self.entry_value.get()), " ", solution)

            self.number_entry.delete(0, "end")
            self.number_entry.insert(0, solution)

    # MY "AC" BUTTON CLEAR SOLUTION
    def clear_button_press(self):
        self.number_entry.delete(0, "end")

    def __init__(self, root):
        self.entry_value = StringVar(root, value="")

        root.title("Calculator")
        root.geometry("530x200")
        root.resizable(width=False, height=False)

        style = ttk.Style()

        style.configure("TButton",
                        font="Serif 15",
                        padding=5)

        style.configure("TEntry",
                        font="Serif 18",
                        padding=10)

        self.number_entry = ttk.Entry(root,
                                      textvariable=self.entry_value, width=65)
        self.number_entry.grid(row=0, columnspan=4)

        # ----- 1st Row -----

        self.button7 = ttk.Button(root, text="7",
                                  command=lambda: self.button_press("7"))
        self.button7.grid(row=1, column=0)

        self.button8 = ttk.Button(root, text="8",
                                  command=lambda: self.button_press("8"))
        self.button8.grid(row=1, column=1)

        self.button9 = ttk.Button(root, text="9",
                                  command=lambda: self.button_press("9"))
        self.button9.grid(row=1, column=2)

        self.button_div = ttk.Button(
            root, text="/",
            command=lambda: self.math_button_press("/")
        )
        self.button_div.grid(row=1, column=3)

        # ----- 2nd Row -----

        self.button4 = ttk.Button(root, text="4",
                                  command=lambda: self.button_press("4"))
        self.button4.grid(row=2, column=0)

        self.button5 = ttk.Button(root, text="5",
                                  command=lambda: self.button_press("5"))
        self.button5.grid(row=2, column=1)

        self.button6 = ttk.Button(root, text="6",
                                  command=lambda: self.button_press("6"))
        self.button6.grid(row=2, column=2)

        self.button_mult = ttk.Button(
            root, text="*",
            command=lambda: self.math_button_press("*")
        )
        self.button_mult.grid(row=2, column=3)

        # ----- 3rd Row -----

        self.button1 = ttk.Button(root, text="1",
                                  command=lambda: self.button_press("1"))
        self.button1.grid(row=3, column=0)

        self.button2 = ttk.Button(root, text="2",
                                  command=lambda: self.button_press("2"))
        self.button2.grid(row=3, column=1)

        self.button3 = ttk.Button(root, text="3",
                                  command=lambda: self.button_press("3"))
        self.button3.grid(row=3, column=2)

        self.button_add = ttk.Button(
            root, text="+",
            command=lambda: self.math_button_press("+")
        )
        self.button_add.grid(row=3, column=3)

        # ----- 4th Row -----

        # TASK: MAKE THE "AC" BUTTON CLEAR THE ENTRY
        self.button_clear = ttk.Button(
            root, text="AC",
            command=lambda: self.clear_button_press()
        )
        self.button_clear.grid(row=4, column=0)

        self.button0 = ttk.Button(root, text="0",
                                  command=lambda: self.button_press("0"))
        self.button0.grid(row=4, column=1)

        self.button_equal = ttk.Button(
            root, text="=",
            command=lambda: self.equal_button_press()
        )
        self.button_equal.grid(row=4, column=2)

        self.button_sub = ttk.Button(
            root, text="-",
            command=lambda: self.math_button_press("-")
        )
        self.button_sub.grid(row=4, column=3)


root = Tk()
calc = Calculator(root)

root.mainloop()
