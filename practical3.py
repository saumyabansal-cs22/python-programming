fileout=open("Student.dat","w")
for i in range(5):
    name=input("Enter name of the student::")
    fileout.write(name)
    fileout.write('\n')
fileout.close()
file=open("Student.dat","r")
while str:
    str=file.readline()
    print(str,end='')
file.close()
