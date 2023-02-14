#WAP to calculate the area of circle radius is entered by the user
#WAP to calculate distance between two co-ordinates
import math
a=eval(input("enter the cordinates=" ))
b=eval(input())
x=eval(input ("enter the second coordinates="))
y=eval(input())
c=(pow((a-b),2)+pow((x-y),2))
d=pow(c,0.5)
print(f"distance={d:0.2f}")
