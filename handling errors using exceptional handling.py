try:
    n=int(input("enter the number:"))
    a=[7,8]
    print(a[n])
except ValueError:
    print("enter valid input")
except IndexError:
    print("Index error")
    
    