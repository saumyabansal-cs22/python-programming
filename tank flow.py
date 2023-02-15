import math 
v=(math.pi)*5**2*10
n=int(input("enter the time of flow of liquid;"))
v2=n*15
if (v2>v):
    print("overflow")
    print(v2-v)
elif (v2==v):
    print("tank is filled")
else:
    print("underflow")
    print(v-v2)
