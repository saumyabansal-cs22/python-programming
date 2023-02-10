import math
for n in range(100,1000):
    l=len(str(n))
    k=n
    s=0
    while n!=0:
       r=n%10
       s=s+pow(r,l)
       n=n//10
    if (k==s):
        print(k)
    
