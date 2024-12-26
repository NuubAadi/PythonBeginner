"""
Write a program that prints minimum and maximum
of five numbers entered by the user
"""
numbers = []
for i in range(5):
    num = int(input("Enter the numbers : "))
    numbers.append(num)

maximum = max(numbers)
minimum = min(numbers)
print(f"The minimum number is: {minimum}")
print(f"The maximum number is: {maximum}")