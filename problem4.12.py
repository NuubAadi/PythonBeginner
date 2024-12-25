"""
Write a pseudocode to calculate the factorial
of a number (Hint: Factorial of 5, written as
5!=5x4x3x2x1).
"""
n = int(input("Enter a number : "))
product=1
for i in range(1,n+1):
    product *= i
print(f"The Factorial of {n} is : {product}")