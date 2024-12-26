"""
Write a function to print the table of a given number.
The number has to be entered by the user
"""
def table(num):
    for i in range(1,11):
        print(f"{num} x {i} = {num*i}")

num = int(input("Enter the number of which table is to be printed :"))
table(num)