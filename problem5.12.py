"""
The formula E = mc2 states that the
equivalent energy (E) can be calculated as the
mass (m) multiplied by the speed of light (c = about
3×108 m/s) squared. Write a program that accepts
the mass of an object and determines its energy
"""
c = 3 * 10**8
mass = float(input("Enter the mass of the object in kilograms: "))

energy = mass * (c**2)
print(f"The energy equivalent of an object with mass {mass} kg is {energy} joules.")
