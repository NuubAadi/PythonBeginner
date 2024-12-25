"""
A dartboard of radius 10 units and the wall it is
hanging on are represented using a two-dimensional
coordinate system, with the board’s center at
coordinate (0,0). Variables x and y store the
x-coordinate and the y-coordinate of a dart that
hits the dartboard. Write a Python expression using
variables x and y that evaluates to True if the dart
hits (is within) the dartboard, and then evaluate the
expression for these dart coordinates:
a) (0,0)
b) (10,10)
c) (6, 6)
d) (7,8)
"""


x = int(input("Enter the value of x :"))
y = int(input("Enter the value of y :"))
x**2 + y**2 <= 100
