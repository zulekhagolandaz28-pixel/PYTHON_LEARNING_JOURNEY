#Q1 Take diameter of a circle as input and calculate its area and circumference.
diameter=float(input("Enter the diameter of the circle: "))
radius=diameter/2
area=3.14*radius**2
circumference=2*3.14*radius
print("Area of the circle is: ", area)
print("Circumference of the circle is: ", circumference)