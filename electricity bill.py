n=int(input("enter no of units of electricity "))
if n<=50:
    c=0.50*n
elif n>50 and n<=150:
    c=(n-50)*0.75+50*0.50
elif n>150 and n<=250:
    c=(n-150)*1.20+100*0.75+50*0.50
else:
    c=n*1.50
p=(20/100)*c
b=c+p
print("your electricity bill=",b)

