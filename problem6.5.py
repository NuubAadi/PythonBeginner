"""
Write a program to generate the sequence: –5, 10,
–15, 20, –25….. upto n, where n is an integer input
by the user.
"""
limit = int(input("Enter the number upto which th series end :"))
for i in range(-5 , limit+1 , 5):
    print(i)