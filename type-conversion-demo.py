'''
Circle Area : πr²
Circle Circumference : 2πr

* Calculate the area and circumference of a circle (pie = 3.14)
'''
pie = 3.14
radius = float(input("Enter the radius of the circle: "))
area = pie * radius ** 2
circumference = 2 * pie * radius
print("The area of the circle is: ", area)
print("The circumference of the circle is: ", circumference)