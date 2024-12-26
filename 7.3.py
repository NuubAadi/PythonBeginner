"""
Write a program that has a user defined function
to accept the coefficients of a quadratic equation
in variables and calculates its determinant. For
example : if the coefficients are stored in the
variables a,b,c then calculate determinant as
b2-4ac. Write the appropriate condition to check
determinants on positive, zero and negative and
output appropriate result.
"""
import cmath  

def find_roots(a, b, c):

    D = b**2 - 4*a*c

    if D > 0:
        root1 = (-b + cmath.sqrt(D)) / (2 * a)
        root2 = (-b - cmath.sqrt(D)) / (2 * a)
        return f"Two real and distinct roots: {root1.real}, {root2.real}"
    
    elif D == 0:
        root = -b / (2 * a)
        return f"One real and repeated root: {root}"
    
    else:
        root1 = (-b + cmath.sqrt(D)) / (2 * a)
        root2 = (-b - cmath.sqrt(D)) / (2 * a)
        return f"Two complex roots: {root1}, {root2}"


a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))


print(find_roots(a, b, c))
