import math
n=int(input("enter the no of digits;="))
i=pow(10,n-1)
while i<pow(10,n):
    l=len(str(i))
    s=0
    k=i
    while (i>0):
        d=i%10
        s=s+d
        i=i//10
    if (k==s):
        print(k)

    
