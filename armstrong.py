n=int(input("enter the number;="))
l=len(str(n))
s=0
k=n
while (n>0):
    d=n%10
    s=s+pow(d,l)
    n=n//10
if (k==s):
    print("Armstrong number")
else:
    print("Not an armstrong number")
