n=int(input())
m=int(input())
for i in range(n):
    if (i==0 or i==m):
        print(' '*(n-i),'* '*(i+1))
    else:
        print(' '*(n-i),'*',' '*((2*i)-1),'*')
    
