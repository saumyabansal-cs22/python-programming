def Bsearch(AR, ITEM):
    beg=0
    last=len(AR)-1
    while (beg<=last):
        mid=(beg+last)/2
        if (ITEM==AR[mid]):
            return mid
        elif (ITEM>AR(mid)):
            beg=mid+1
        else:
            last=mid-1
    else:
        return False
#__main--
n=int(input("Enter desired linear-list size(max.50)..."))
print("\nEnter elements for linear list in ascending order\n")
AR=[0]*n
for i in range(n):
    AR[i]=int(input("Element"+str(i)+":"))

ITEM=int(input("\n Enter Element to be searched for..."))
index=Bsearch(AR, ITEM)

if index:
    print("\nElement found at index:",index,",Position:",(index+1))
else:
    print("\n Sorry!! Given element could not be found.\n")
