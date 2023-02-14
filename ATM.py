amount=int(input("enter the amount"))
#logic section
amount=amount-100  #coz we needed atleast one 100rs note
twok=amount//2000
m=(amount-(twok*2000))
fiveh=m//500
n=(m-(fiveh*500))
twoh=n//200
oneh=(n-(twoh*200))//100+1
#print section
print(f'no of 100 notes={oneh}')
print(f'no of 200 notes={twoh}')
print(f'no of  500 notes={fiveh}')
print(f'no of 2000 notes={twok}')
