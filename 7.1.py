"""
Write a program to check the divisibility of a
number by 7 that is passed as a parameter to the
user defined function.
"""
def divisible(num):
    if num % 7 == 0 :
        return True
    else:
        return False
    
num = int(input("Enter the number :"))
print(divisible(num))

