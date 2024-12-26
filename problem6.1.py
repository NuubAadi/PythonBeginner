"""
Write a program that takes the name and age of the
user as input and displays a message whether the
user is eligible to apply for a driving license or not.
(the eligible age is 18 years).
"""
name = input("Enter your name : ")
age = int(input("Enter your age : "))
if age >= 18 :
    print("You are Eligible for driving.")
else:
    print("You are not Eligible for driving.")