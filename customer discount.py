a=int(input("enter the total shopping amount"))
g=a-((20/100)*a)
s=a-((10/100)*a)
b=a-((5/100)*a)
if (a>25000):
    print("GOLD customer")
    print("your shopping amount=",g)
elif (a>=10000 and a<25000 ):
    print("SILVER customer")
    print("your shopping amount=",s)
else:
    print("BRONZE customer")
    print("your shopping amount=",b)
