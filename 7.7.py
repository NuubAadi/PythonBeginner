import math

def area_square(side):
    return side * side

def perimeter_square(side):
    return 4 * side


def area_rectangle(length, width):
    return length * width

def perimeter_rectangle(length, width):
    return 2 * (length + width)


def area_triangle(base, height):
    return 0.5 * base * height


def perimeter_triangle(a, b, c):
    return a + b + c


def area_circle(radius):
    return math.pi * radius * radius


def perimeter_circle(radius):
    return 2 * math.pi * radius


def surface_area_cylinder(radius, height):
    return 2 * math.pi * radius * (radius + height)


def volume_cylinder(radius, height):
    return math.pi * radius * radius * height

def main():
    print("Select the shape:")
    print("1. Square")
    print("2. Rectangle")
    print("3. Triangle")
    print("4. Circle")
    print("5. Cylinder")

    choice = int(input("Enter the number corresponding to the shape: "))

    if choice == 1:  # Square
        side = float(input("Enter the side length of the square: "))
        print(f"Area of square: {area_square(side)}")
        print(f"Perimeter of square: {perimeter_square(side)}")

    elif choice == 2:  # Rectangle
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        print(f"Area of rectangle: {area_rectangle(length, width)}")
        print(f"Perimeter of rectangle: {perimeter_rectangle(length, width)}")

    elif choice == 3:  # Triangle
        base = float(input("Enter the base of the triangle: "))
        height = float(input("Enter the height of the triangle: "))
        print(f"Area of triangle: {area_triangle(base, height)}")
        side1 = float(input("Enter the first side of the triangle: "))
        side2 = float(input("Enter the second side of the triangle: "))
        side3 = float(input("Enter the third side of the triangle: "))
        print(f"Perimeter of triangle: {perimeter_triangle(side1, side2, side3)}")

    elif choice == 4:  # Circle
        radius = float(input("Enter the radius of the circle: "))
        print(f"Area of circle: {area_circle(radius)}")
        print(f"Perimeter (Circumference) of circle: {perimeter_circle(radius)}")

    elif choice == 5:  # Cylinder
        radius = float(input("Enter the radius of the cylinder: "))
        height = float(input("Enter the height of the cylinder: "))
        print(f"Surface area of cylinder: {surface_area_cylinder(radius, height)}")
        print(f"Volume of cylinder: {volume_cylinder(radius, height)}")

    else:
        print("Invalid choice! Please select a valid shape.")


if __name__ == "__main__":
    main()
