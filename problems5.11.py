"""
Write a program that asks the user
to enter their name and age. Print a
message addressed to the user that tells the user
the year in which they will turn 100 years old
"""
name = input("Enter your name :")
age = int(input("Enter your age :"))
current_year = 2024
year_turn_100 = 2024 + 100 - age
print(f"You will turn 100 in the year {year_turn_100}")
