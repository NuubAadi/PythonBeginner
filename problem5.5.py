"""
Write a Python program to calculate the amount
payable if money has been lent on simple interest.
Principal or money lent = P, Rate of interest = R%
per annum and Time = T years. Then Simple Interest
(SI) = (P x R x T)/ 100.
 Amount payable = Principal + SI.
 P, R and T are given as input to the program.
 """
principal = int(input("Enter the principal :"))
Rate_of_interest = int(input("Enter the Rate_of_interest :"))
time = int(input("Enter the Time :"))

SI = (principal*Rate_of_interest*time)/100
Amount = principal+ SI
print(f"The Simple Interest is :{SI}")
print(f"The Amount Payable is :{Amount}")