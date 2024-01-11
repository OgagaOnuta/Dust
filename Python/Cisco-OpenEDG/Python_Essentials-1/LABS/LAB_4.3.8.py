'''
Converting fuel consumption
'''

# 1 American mile = 1609.344 metres = 1.609344 km
# 1 American gallon = 3.785411784 litres

# CiscoEDG HINT


def litres_100km_to_miles_gallon(litres):
	miles = 100 / 1.609344
	gallons = litres / 3.785411784

	return (miles / gallons)


def miles_gallon_to_litres_100km(miles):
	km100 = (miles * 1.609344) / 100
	litres = 3.785411784

	return (litres / km100)


print(litres_100km_to_miles_gallon(3.9))
print(litres_100km_to_miles_gallon(7.5))
print(litres_100km_to_miles_gallon(10.))
print(miles_gallon_to_litres_100km(60.3))
print(miles_gallon_to_litres_100km(31.4))
print(miles_gallon_to_litres_100km(23.5))
