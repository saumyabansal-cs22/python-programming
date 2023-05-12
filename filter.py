def func(a):
    return a>2
l=[1,5,8,9,6]
n=filter(func,l)
print(list(n))