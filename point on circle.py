import math
a=int(input())
b=int(input())
r=int(input("radius of circle;"))
print("enter coordinates of point p;")
x=int(input())
y=int(input())
d=math.sqrt((pow((x-a),2)+pow((y-b),2)))
if (d>r):
    print("point outside the circle;")
elif (d==r):
    print("point on the circle;")
else:
    print("point inside the circle:")
