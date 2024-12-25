import math

def compute_height(length, angle):
    angle_in_radians = math.radians(angle)
    height = length * math.sin(angle_in_radians)
    return height

test_cases = [
    (16, 75),
    (20, 0),
    (24, 45),
    (24, 80)
]
for length, angle in test_cases:
    height = compute_height(length, angle)
    print(f"Length: {length} feet, Angle: {angle} degrees => Height: {height:.2f} feet")
