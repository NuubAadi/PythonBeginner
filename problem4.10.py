"""
Write an algorithm that accepts four numbers as
input and find the largest and smallest of them.

"""
numbers = []
for i in range(4):
    number = int(input(f"Number {i+1} is : "))
    numbers.append(number)
largest= float('-inf')
smallest=float('inf')
for number in numbers:
    if number>largest:
        largest=number
    if number<smallest:
        smallest=number
print(f"The Largest is {largest}")
print(f"The Smallest is {smallest}")
