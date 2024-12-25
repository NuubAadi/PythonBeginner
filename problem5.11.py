"""
The volume of a sphere with radius r is 4/3πr3. Write
a Python program to find the volume of spheres with
radius 7cm, 12cm, 16cm, respectively.
"""
def volume_sphere(radius):
    return (4/3*3.14)*(radius**3)

a = 7
print(round(volume_sphere(a),3))
b = 12
print(round(volume_sphere(b),3))
c = 16
print(round(volume_sphere(c),3))