"""
Write a program to repeat the string ‘‘GOOD
MORNING” n times. Here ‘n’ is an integer
entered by the user.
"""
n = int(input("Enter value of n :"))
for i in range(n):
    print("Good Morning")

"""
Write a program to find average of three numbers.
"""
a = int(input("Enter Number 1 :"))
b = int(input("Enter Number 2 :"))
c = int(input("Enter Number 3 :"))
average = (a+b+c)/3
print(average)