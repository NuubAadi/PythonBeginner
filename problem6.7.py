"""
Write a program to find the sum of digits of an
integer number, input by the user.
"""
num = int(input("Enter an Number : "))
sum = 0
while(num>0):
    d = num % 10
    sum += d
    num = num//10
print(f"The sum of the number is {sum}")
