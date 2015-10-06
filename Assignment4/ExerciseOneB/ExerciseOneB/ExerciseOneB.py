celsius = -273.16
while celsius < -273.15:
    celsius = float(input("Enter in a celsius to convert to kelvin \n"))
    kelvin = celsius + 273.15
    output = round(kelvin,2)
print output, "kelvin"