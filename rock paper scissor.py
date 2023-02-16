p=input("enter choice of PLAYER 1: (Rock,scissors,paper)")
q=input("Enter choice of PLAYER 2: (Rock,scissors,paper)")
if (p=="Rock"):
    if(q=="paper"):
        print("Player 1 loses;")
    elif(q=="scissors"):
        print("Player 1 wins;")
    else:
        print("Tie")
elif(p=="paper"):
    if (q=="Rock"):
        print("Player 1 wins;")
    elif (q=="scissors"):
        print("Player 1 loses;")
    else:
        print("Tie")
elif(p=="scissors"):
    if(q=="Rock"):
        print("Player 1 loses;")
    elif(q=="paper"):
        print("Player 1 wins;")
    else:
        print("Tie")
else:
    print("Enter valid choice;")
