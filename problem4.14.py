"""
Draw a flowchart to check whether a given number
is an Armstrong number. An Armstrong number of
three digits is an integer such that the sum of the
cubes of its digits is equal to the number itself. For
example, 371 is an Armstrong number since 3**3 +
7**3 + 1**3 = 371.
"""
number = int(input("Enter a three-digit number: "))
sum=0
original_number = number
while(number>0):
    d=number%10
    sum += (d**3)
    number=number//10
if sum == original_number:
    print("It is an Armstrong Number")
else:
    print("It is not an Armstrong Number")
