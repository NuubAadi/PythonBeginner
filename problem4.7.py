"""
Write pseudocode that will perform the following:
a) Read the marks of three subjects: Computer
Science, Mathematics and Physics, out of 100
b) Calculate the aggregate marks
c) Calculate the percentage of marks
"""
a = int(input("Enter Science Marks:"))
b = int(input("Enter Maths Marks:"))
c = int(input("Enter Physics Marks:"))
aggregate_marks = a+b+c
print(f"The total marks is :{aggregate_marks}")
percentage = (aggregate_marks*100)/300
print(f"Percentage is : {percentage}")