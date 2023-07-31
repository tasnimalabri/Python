import math
def polygon1(num, side):
    area = (number * (length ** 2))/(4 * math.tan(math.pi/number))
    return area, length, number
length  = float(input("Enter the length of each side of Polygon (in meters): "))
number  = int(input("Enter the number of sides: "))

area_polyon = polygon1(length, number)

print(area_polyon)