def traverse(ar):
    size=len(ar)
    for i in range(size):
        print(ar[i],end=',')

#--main--
size=int(input("Enter the size of linear list to be input:"))
ar=[0]*size
print("Enter elements for the linear list")
for i in range(size):
    ar[i]=int(input("Element"+str(i)+":"))
print("Traversing the list:")
traverse(ar)
