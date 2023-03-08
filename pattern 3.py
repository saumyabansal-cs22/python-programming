""""
                 Z
             Z  X
         Z X  Y
   Z  X  Y  W
Z X  Y  W  V

"""
n=91
for i in range (1,6):
    for j in range(1,6):
        if (i+j<=5):
            print("   ",end=' ')
        else:
            m=i+j-5
            print(chr(n-m) ,end=' ')
    print()
