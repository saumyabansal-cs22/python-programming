"""Ms. Puja having some toys and she want to arrange all the
toys with their names that toys can be chained to form a circle by names.
The toy X can be placed in front of another toy Y in a circle if the last character of X is same as the first character of Y.

For example, the toys names are ['chair', 'height', 'racket', 'touch', 'tunic'] can form the following circle:
chair --> racket --> touch --> height --> tunic --> chair"""

n=int(input())
l=input().split()
le=len(l)
l1=[]
l2=[]
for i in l:
    lee=len(i)
    l1.append(i[0])
    l2.append(i[lee-1])
l1=sorted(l1)
l2=sorted(l2)
if(l1==l2):
    print("True")
else:
    print("False")
