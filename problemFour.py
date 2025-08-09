# Muhammad Haroon Nasir
# August 6th, 2025

# defines a function that takes radius as parameter and returns the area. Asks user for radius, and calls area function with radius value.
# The return statement is tored in to a variable and then printed

def areaOfCircle(radius):
    pi = 3.14
    area = pi * radius**2
    return area

radius = int(input("What is the radius of the circle"))
area = areaOfCircle(radius)

print(f"Heres the area for the circle you asked for!  {area}")