a=eval(input("enter first side"))
b=eval(input("enter second side"))
c=eval(input("enter third side"))
if (a+b>c and b+c>a and a+c>b):
    print("valid triangle")
else:
    print("invalid triangle")
