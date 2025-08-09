# Muhammad Haroon Nasir
# August 6th, 2025

# Defines a function that takes miles and gallons as parameters and returns mpg.
# User is prompted for miles driven and gallons used, function is then called and passed the given parameters.
# Return statement of function call is saved in to variable and called in print statement

def mpgCalc(miles, gallons):
    mpg = miles / gallons
    return mpg

miles = int(input("How many miles is the car driven?"))
gallons = int(input("How many gallons has the car used"))
mpg = mpgCalc(miles, gallons)
print(f"the car uses {mpg} miles per gallon")