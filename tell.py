with open("myfile.txt","r") as f:
    print(f.tell())
    print(f)
    f.seek(10)
    print(f.tell())
    m=f.read(5)
    print(m)
    g=f.tell()
    print(g)
    f.close()