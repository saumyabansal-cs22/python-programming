def lsearch(ar,item):
    i=0
    while i<len(ar) and ar[i]!=item:
        i+=1
    if i<len(ar):
            return i
    else:
            return False

#__main__
mylist=[10,20,30,40,50,60,70]
print("The list in sorted order is::")
print(mylist)
item=int(input("Enter element to be deleted:"))

position=lsearch(mylist, item)
if position:
    del mylist[position]
    print("The list after deleting",item,"is")
    print(mylist)
else:
    print("\nSORRY! No such element in the list")
