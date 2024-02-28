import math
radius = int(input('Radius: '))

def area(radius):
  area = math.pi * radius**2
  return area

print(f'The area is: {area(radius)}')