"""
Write a program to calculate in how many days a
work will be completed by three persons A, B and
C together. A, B, C take x days, y days and z days
respectively to do the job alone. The formula to
calculate the number of days if they work together
is xyz/(xy + yz + xz) days where x, y, and z are given
as input to the program.
"""
x = int(input("Enter the no. of days taken by A to complete the job :"))
y = int(input("Enter the no. of days taken by B to complete the job :"))
z = int(input("Enter the no. of days taken by C to complete the job :"))
work_together = (x*y*z)/((x*y)+(y*z)+(x*z))
print(f"If they work together they will take {round(work_together,2)} days")