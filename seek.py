with open("myfile.txt","r") as f:
    f.seek(10)
    m=f.read(5)
    print(m)
    f.close()
