"""
Write a program that implements a user defined
function that accepts Principal Amount, Rate,
Time, Number of Times the interest is compounded
to calculate and displays compound interest.
(Hint: amount=P*(1+r/n)nt)
"""
def amount(principal_amout,rate,time,number_of_times):
   amount = principal_amout*(1+rate/number_of_times)**(number_of_times*time)
   return amount

principal = int(input("Enter the principal amount : "))
rate = float(input("Enter the rate of interest : "))
time = int(input("Enter the time : "))
no_of_time = int(input("Enter the number of times : "))
amount = amount(principal,rate,time,no_of_time)
print (round(amount,2))
CI = amount - principal
print(round(CI,2))