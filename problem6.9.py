"""
Write a program to find the grade of a student when
 grades are allocated as given in the table below.
Percentage of Marks Grade
Above 90%   A
80% to 90%  B
70% to 80%  C
60% to 70%  D
Below 60%   E
 Percentage of the marks obtained by the student is input
to the program.
"""
percentage = int(input("Enter the percentage : "))
if percentage >= 90 :
    print("A grade")
elif percentage<90 and percentage>=80 : 
    print("B grade")
elif percentage<80 and percentage>=70 : 
    print("C grade")
elif percentage<70 and percentage>=60 : 
    print("D grade")
elif percentage<60 :
    print("E grade")