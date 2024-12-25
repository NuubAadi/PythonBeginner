'''
Write a Python program to convert temperature in
degree Celsius to degree Fahrenheit. If water boils
at 100 degree C and freezes as 0 degree C, use the
program to find out what is the boiling point and
freezing point of water on the Fahrenheit scale.
 (Hint: T(°F) = T(°C) × 9/5 + 32)
 '''
# Celsius = int(input("Enter Celsius :"))
# Fahrenheit = (celsius * 9/5 )+ 32
# print(f"T(°C)= {Fahrenheit}")
def celsius_to_fahrenite(celsius):
    return (celsius * 9/5 )+ 32

Celsius = int(input("Enter Celsius :"))
print(celsius_to_fahrenite(Celsius))
boiling_point1 = 100
freezing_point1 = 0
boiling_point2 = celsius_to_fahrenite(boiling_point1)
freezing_point2 = celsius_to_fahrenite(freezing_point1)
print(f"Freezing point of water: {freezing_point1}°C = {freezing_point2}°F")
print(f"Boiling point of water: {boiling_point1}°C = {boiling_point2}°F")


