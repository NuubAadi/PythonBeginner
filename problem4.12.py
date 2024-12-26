"""
Write a pseudocode to calculate the factorial
of a number (Hint: Factorial of 5, written as
5!=5x4x3x2x1).
"""
# n = int(input("Enter a number : "))
# product=1
# for i in range(1,n+1):
#     product *= i
# print(f"The Factorial of {n} is : {product}")

def factorial(num):
    if num == 0 or num == 1 :
        return 1
    return num*factorial(num-1)

num = int(input("Enter the number :"))
print(f"The factorial of {num} is : {factorial(num)}")