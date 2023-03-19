n=int(input())
w=int(input())
m=n//2
for i in range(n):
    for j in range(w):
        if i==0 or i==m or i==n-1:
            print('*',end=' ')
        elif j==0 or j==w-1:
            print('*',end=' ')
        else: 
            print('  ',end=' ')
    print()
