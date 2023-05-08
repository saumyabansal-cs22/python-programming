"""You are given a 2-D array with dimensions NXM.
Your task is to perform the //sum// tool over axis  and then find the //product//  of that result."""

import numpy as np
m,n=map(int,input().split())
l=[]
m=1
for i in range(n):
    l1=list(map(int,input().split()))
    l.append(l1)
l2=np.sum(l,axis=0)
for i in l2:
    m*=i
print(m)
