"""
Write a program that has a user defined function
to accept 2 numbers as parameters, if number 1
is less than number 2 then numbers are swapped
and returned, i.e., number 2 is returned in place
of number1 and number 1 is reformed in place of
number 2, otherwise the same order is returned.
"""

def number(num1,num2):
    if num1 < num2 :
        temp = num1
        num1 = num2
        num2 = temp
        return (num1,num2)
    else:
        return (num1,num2)
    
num1 = int(input("Enter the number 1 : "))
num2 = int(input("Enter the number 2 : "))
print(number(num1,num2))