n=int(input())
m=(n//2)+1
for i in range(1,n+1):
    if i<=m:
        print("  "*(m-i),"*"*(2*i-1),end='')
    else:
        print("  "*(i-m),"*"*(2*(n-i)+1),end='')
    print()
