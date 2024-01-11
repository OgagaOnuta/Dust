'''
Operators and expressions - 2
'''

hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes: "))

hours_in_mins = (mins + dura) // 60
mins = (mins + dura) % 60
hour = (hour + hours_in_mins) % 24

print(str(hour) + ":" + str(mins))
