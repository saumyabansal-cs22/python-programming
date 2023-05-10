def func():
    try:
        a=int(input())
        print(a**4)
        return 1
    except:
        print("error occured")
        return 0
    # finally:
    print("Program finally ends!")
x=func()
print(x)