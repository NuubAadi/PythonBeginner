"""
Write a program to find the sum of 1+ 1/8 +
1/27......1/n3, where n is the number input by the
user.
"""
n = int(input("Enter an number : "))
sum_series = 0
for i in range(1,n+1):
    sum_series += 1 / (i**3)

print(f"The sum of series is : {round(sum_series,2)}")