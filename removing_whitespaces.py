# def remove_newlines(fname):
#     flist = open(fname).readlines()
#     return [s.rstrip('\n') for s in flist]
# print(remove_newlines("myfile.txt"))
f=open("myfile.txt","r+")
m=f.readlines()
for i in m:
    i.rstrip('\n')
print(f.read())
