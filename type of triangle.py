import math
a=int(input("Enter the first side;"))
b=int(input("Enter the second side;"))
c=int(input("Enter the third side;"))
if (a+b>c or a+c>b or b+c>a):
    if ((pow(c,2)==pow(b,2)+pow(a,2)) or (pow(a,2)==pow(b,2)+pow(c,2)) or  (pow(b,2)==pow(a,2)+pow(c,2))):
        print("Right angled triangle;")
    if (a==b):
        if(b==c):
            print("equivalateral;")
        else:
            print("isoceles;")
    if (a!=b):
        if (b!=c):
            print("scalene")
        else:
            print("isoceles")
else:
    print("Not a valid triangle;")
