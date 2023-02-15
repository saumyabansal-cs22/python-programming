s=0
for i in range (1,31):
    if i%2==0:
        if i==10 or i==20:
            continue
        else:
            s=s+i
print("Required sum=",s)
