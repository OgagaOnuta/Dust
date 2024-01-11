#!/usr/bin/python3

invst = float(input("Enter Investment: "))
intrst = float(input("Enter Interest: ")) / 100
period = float(input("How many year(s) period: "))
freq = float(input("Frequency of interest compounded annually: "))

Comp_Intrst = invst * ((1 + (intrst / freq)) ** (freq * period))

print("{:.2f}".format(Comp_Intrst))
