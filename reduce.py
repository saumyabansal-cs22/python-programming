from functools import reduce
l=[7,8,9,5,6]
def sum(x,y):
    return x+y
n=reduce(sum,l)
print(n)