"""
Write a program to swap two numbers without
using a third variable.
"""
a = int(input("Enter Number 1 :"))
b = int(input("Enter Number 2 :"))
a = a + b 
b = a - b  
a = a - b  
print(a, b)
