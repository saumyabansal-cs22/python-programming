n=5
for i in range(n):
    print("  "*(n-i)+"*"*(i))
        
"""
Try these:

           Z
        Z Y
    Z Y X
Z Y X W
"""
n=5
for i in range(n):
    if i==0 or i==n-1:
        print("*"*(i+1))
    else:
        print("*","  "*(i-1),"*",sep='')
"""
hw question

            A
        B     B
    C            C
D                   D
   C             C
        B     B
            A
"""

