f=open("myfile.txt","r")
while True:
    m=f.readline()
    print(m)
    if not m:
        break
    