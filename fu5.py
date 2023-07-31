import math
def square(a):
    area = (a**2)
    return area, a
a  = int(input("Enter the a "))


area_square = square(a)

print(area_square)

def circle(pi , r):
    area = (pi * r**2)
    return area, pi, r

r = int(input("Enter the r"))
pi = float(input("Enter the pi"))

area_circle = circle(r , pi)

print(area_circle)
def rectangular(Length , Width):
    area = (Length * Width)
    return area, Length, Width
Length = int(input("Enter the Length "))
Width = int(input("Enter the Width"))

area_rectangular = rectangular(Length, Width)

print(area_rectangular)
def cylinder(pi , r , h):
    area = (2 * pi * r * h + 2 * pi * r**2)
    return area, pi , r , h
r = int(input("Enter the r "))
h = int(input("Enter the height"))
pi = float(input("Enter the pi"))

area_cylinder = cylinder(pi , r , h)

print(area_cylinder)

def triangle(b, h):
    area = ((h*b)/2)
    return area, b, h
b = int(input("Enter the b "))
h = int(input("Enter the height"))


area_triangle = triangle(h, b)

print(area_triangle)

def square(a):
    area = (a**2)
    return area, a
def circle(pi , r):
    area = (pi * r**2)
    return area, pi, r
def rectangular(Length , Width):
    area = (Length * Width)
    return area, Length, Width
def cylinder(pi , r , h):
    area = (2 * pi * r * h + 2 * pi * r**2)
    return area, pi , r , h
def triangle(b, h):
    area = ((h*b)/2)
    return area, b, h
def main():
    while True:
    print("choose the number (1-6)")
    print("1.square")
    print("2.circle")
    print("3.rectangular")
    print("4.cylinder")
    print("5.triangle")
    print("6.quit")
    
    choice = int(input("choose the number 1-6"))
    if choice == 1:
        a  = int(input("Enter the a "))
        area_square = square(a)
        print(area_square)
    elif choice == 2:
        r = int(input("Enter the r"))
        pi = float(input("Enter the pi"))

        area_circle = circle(r , pi)
    
    elif choice == 3:
        Length = int(input("Enter the Length "))
        Width = int(input("Enter the Width"))

        area_rectangular = rectangular(Length, Width)

print(area_rectangular)
    elif choice == 4:
        r = int(input("Enter the r "))
        h = int(input("Enter the height"))
        pi = float(input("Enter the pi"))

        area_cylinder = cylinder(pi , r , h)

        print(area_cylinder)
    elif choice == 5:
        b = int(input("Enter the b "))
        h = int(input("Enter the height"))


        area_triangle = triangle(h, b)

        print(area_triangle)
        
    else :
        exit()
    
    
    
    
    


