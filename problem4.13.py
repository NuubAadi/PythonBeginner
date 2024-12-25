"""
Following is an algorithm to classify numbers as
“Single Digit”, “Double Digit” or “Big”.
Classify_Numbers_Algo
INPUT Number
IF Number < 9
 "Single Digit"
Else If Number < 99
 "Double Digit"
Else
 "Big"
Verify for (5, 9, 47, 99, 100 200) and correct the
algorithm if required
"""
n = int(input("Enter an number :"))
if n <= 9:
 print("Single Digit")
elif n <= 99:
 print("Double Digit")
else:
 print("Big")