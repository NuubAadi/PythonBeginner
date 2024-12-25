"""
. Write an algorithm to display the total water bill charges
of the month depending upon the number of units
consumed by the customer as per the following criteria:
• for the first 100 units @ 5 per unit
• for next 150 units @ 10 per unit
• more than 250 units @ 20 per unit
Also add meter charges of 75 per month to calculate
the total water bill .
"""
units = int(input("Enter the units consumed :"))
if units<=100:
     Total_Bill = (units*5) + 75
     print(f"Total water bill is :{Total_Bill}")
elif units>100 and units<=250:
    Total_Bill = (100*5)+((units-100)*10) + 75
    print(f"Total water bill is :{Total_Bill}")
elif units>250:
    Total_Bill = (100*5)+((150)*10)+((units-250)*20) +75
    print(f"Total water bill is :{Total_Bill}")


