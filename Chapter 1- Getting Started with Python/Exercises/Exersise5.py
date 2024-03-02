# I imported the math library to use pi
import math

# asks the user to input radius using an input function
radius = int(input('Radius: '))

# made a defined function on how to calculate area
def area(radius):
    # using the imported math to get pi
    area = math.pi * radius**2
    # returns the result to the function
    return area

# prints the area using an fstring
print(f'The area is: { area(radius) }')
