str=input("Enter a name =")
l=len(str)
m=l//2
k=0
for i in range(0,m):
    if (str[i]==str[l-i-1]):
        k=1
    else:
        k=0
if (k==1):
    print("palindrome string;")
else:
    print("Not a palindrome string;")
