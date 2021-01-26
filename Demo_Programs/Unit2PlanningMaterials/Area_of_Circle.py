import math


def areaOfCircle():
	x1 = 2
	y1 = 4
	x2 = 2
	y2 = 8

	r = ((y2 - y1)**(2) + (x2 - x1)**(2))**(1/2)

	a = 3.14159*r**2

	print(a)

areaOfCircle()