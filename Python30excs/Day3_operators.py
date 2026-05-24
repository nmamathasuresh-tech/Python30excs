age=25
height=2.75
print(age)
print(height)   

complex_number=2+3j;
print(complex_number)

base=int(input("Enter the base of the triangle: " ))
print(base)
height=int(input("Enter the height of the triangle: " ))
print(height)
area_of_triangle=0.5*base*height
print("The area of the triangle is", area_of_triangle)


side_a=int(input("Enter the length of side a: "))
side_b=int(input("Enter the length of side b: "))       
side_c=int(input("Enter the length of side c: "))
perimeter_of_triangle=side_a+side_b+side_c
print("The perimeter of the triangle is", perimeter_of_triangle)

length=int(input("Enter the length of the rectangle: "))
width=int(input("Enter the width of the rectangle: "))      
area_of_rectangle=length*width
print("The area of the rectangle is", area_of_rectangle)
perimeter_of_rectangle=2*(length+width)
print("The perimeter of the rectangle is", perimeter_of_rectangle)

#Calculate the slope, x-intercept and y-intercept of y = 2x -2

m= 2
b=-2
y_intercept=(m*0,b)
x_intercept=(-b/m,0)
print("Slope:", m)
print("x-intercept:", x_intercept)
print("y-intercept:", y_intercept)

# Points
x1, y1 = 2, 2
x2, y2 = 6, 10
slope = (y2 - y1) / (x2 - x1)
print("Slope of the line connecting points (2, 2) and (6, 10):", slope)
#euclidean distance
distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
print("Euclidean distance between points (2, 2) and (6, 10):", distance)

# Compare slopes

if m == slope:
    print("\nThe slopes are equal.")
else:
    print("\nThe slopes are different.")

#Calculate the value of y (y = x^2 + 6x + 9).ry to use different x values and figure out at what x value y is going to be 0.

    for x in range(-10, 11):
     y = x**2 + 6*x + 9
    print("x =", x, " y =", y)

    if y == 0:
        print("y becomes 0 when x =", x)

        