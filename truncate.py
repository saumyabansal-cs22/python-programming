with open("myfile.txt","w") as f:
    f.write("hello world")
    f.truncate(5)
    f.close()