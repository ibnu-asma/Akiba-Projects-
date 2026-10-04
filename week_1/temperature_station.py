#Goal
#Practice mathematical expressions and unit conversion.
#Create a temperature conversion program.
#The user enters a temperature in Celsius.
#Convert it to Fahrenheit.
#
#Formula:
#F = (C × 9/5) + 32
#Then display both temperatures.
#Example
#Temperature: 25°C
#
#Celsius: 25°C
#Fahrenheit: 77°F
#Bonus
#Also convert Fahrenheit → Celsius.
#Concepts
#float() • arithmetic • formatted output
#
line = "========================================================================="
mode = input("Press 1 for celsius conversion, 2 for Fahrenheit: ")
if mode == "1":
    celsius = float(input("Enter Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
else:
    fahrenheit = float(input("Enter Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5/9

output = f"""
            {line}
            Celsius = {celsius}
            Fahrenheit = {fahrenheit}
    """
print(output)


