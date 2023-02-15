n=int(input("enter the number;"))
k=n
d=0
while(n>0):
    r=n%10
    d=d*10+r
    n=n//10
if  k==d:
    print("Palindrome number;")
else:
    print("Not a palindrome number")
