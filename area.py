import math
area = {}
shape = input()
if shape == 'square':
    side = float(input())
    area = (side * side)
    rounded_number = round(area, 3)
    print(rounded_number)
elif shape == 'rectangle':
    side1 = float(input())
    side2 = float(input())
    area = (side1 * side2)
    rounded_number = round(area, 3)
    print(rounded_number)
elif shape == 'circle':
    radius = float(input())
    area = (3.14 * (radius ** 2))
    rounded_number = round(area, 3)
    print(rounded_number)
elif shape == 'triangle':
    base = float(input())
    height = float(input())
    area = ((1/2) * base * height)
    rounded_number = round(area, 3)
    print(rounded_number)