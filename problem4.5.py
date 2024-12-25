"""
Suppose you are collecting money for something.
You need ` 200 in all. You ask your parents, uncles
and aunts as well as grandparents. Different people
may give either ` 10, ` 20 or even ` 50. You will collect
till the total becomes 200. Write the algorithm
"""

total_collected = 0
while total_collected < 200:
    donation = int(input("Enter a donation amount (10, 20, or 50): "))
    
    if donation in [10, 20, 50]:
        total_collected += donation 
        print(f"Total collected so far: {total_collected}")
    else:
        print("Invalid donation amount. Please enter 10, 20, or 50.")

print(f"Total collected: {total_collected}. You have enough money!")
