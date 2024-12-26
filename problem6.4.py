"""
Write a program to check if the year entered by the
user is a leap year or not.
"""
year = int(input("Enter the year : "))
if year % 4 == 0 :
    print("It is a Leap year.")
else:
    print("It is not a Leap year.")