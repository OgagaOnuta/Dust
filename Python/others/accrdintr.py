#!/usr/bin/python3

'''
Accrued Interest for Monthly Earnings
'''

# Receive investment and interest inputs from user
invst = float(input("Monthly Investment: "))
intrst = float(input("Interest Rate: ")) * .01

# Convert Annual Interest to Daily Interest
intrst_daily = intrst / 365

# Get Number of Months invested
n = int(input("How many year(s) period: ")) * 12

# Store original Investment
curnt_invst = invst

i = 1
# Cycle through years using a loop
while (i <= n):
    # Calculate Accrued Interest
    accint = intrst_daily * 30 * curnt_invst
    curnt_invst = curnt_invst + accint + invst
    # Print out earnings
    print("Month {:2d}: Accrued Interest: {:>10.2f}".format(i, accint))
    print("Month {:2d}: Current Investment: {:>8.2f}".format(i, curnt_invst))
    i += 1
