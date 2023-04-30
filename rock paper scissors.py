import random
def game(comp,you):
    if comp==1:
        if you==3:
            return True 
        elif you==2:
            return False
    elif comp==2:
        if you==1:
            return True 
        elif you==3:
            return False
    elif comp==3:
        if you==1:
            return True 
        elif you==2:
            return False
    elif comp==you:
        return None
    else:
        return 2
print("Computer's turn:?")
comp=random.randint(1,3)
you=int(input("Player's turn:: Choose Rock(1) or Paper(2) or Scissor(3)::"))
a=game(comp,you)
print("Computer chose:",comp)
print("You chose:",you)
while True:
    if a==True:
        print("you win")
        break
    elif a==False:
        print("you lose")
        break
    elif a==None:
        print("The game is a tie//")
        break
    elif a==2:
        print("enter valid choice")
        break
else:
    print("The game ends")
    
