# Created by: Mr. Coxall
# Created on: Oct 2020
#
# This program calculates the area and perimeter of a rectangle

# variables
length = 0
width = 0
area = 0
perimeter = 0

# Input
length = int(input("Enter the length of the rectangle: "))
width = int(input("Enter the width of the rectangle: "))

# Process
perimeter = 2 * (length + width)
area = length * width

# output
print("The area of your rectangle is: " + str(area))
print("The perimeter of your rectangle is: " + str(perimeter))
print("Done")