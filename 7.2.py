"""
Write a program that uses a user defined function
that accepts name and gender (as M for Male,
F for Female) and prefixes Mr/Ms on the basis of
the gender.
"""
def name_gender(name,gender):
    if gender.upper() == "M" :
        return "Mr. " + name
    elif gender.upper() == "F":
        return "Mrs. " + name
    else:
        return "Invalid inputs"
    
name = input("Enter your name :")
gender = input("Enter your gender (M or F) : ")
print(name_gender(name,gender))