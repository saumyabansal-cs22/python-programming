s=int(input("enter salary of employee;="))
if s<=10000:
    s=(20/100)*s +(80/100)*s+s
elif(s>10000 and s<=20000):
    s=(25/100)*s +(90/100)*s+s
elif(s>20000):
    s=(30/100)*s +(95/100)*s+s
print("Gross salary;=",s)
