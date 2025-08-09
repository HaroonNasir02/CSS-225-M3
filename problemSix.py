# Muhammad Haroon Nasir
# August 6th, 2025

# Function takes temp as parameter and returns conversion to celsius. user is prompted for farenheight value, which is plugged in to function.
# Return value from function call is saved in a variable and then printed out

def farenheightToCelsius(temp):
    celsius = (temp - 32) * (5/9)
    return temp

degreeF = int(input("Please enter farenhieght value to convert to celsius"))
degreeC = farenheightToCelsius(degreeF)

print(f"{degreeF} degrees farenheight is equal to {degreeC} degrees celsius")