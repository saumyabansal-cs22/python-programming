c=input("enter the character;")
if len(c)==1:
    if (c>='0' and c<='9'):
        print("digit")
    elif (c>'a' and c<'z') or (c>'A' and c<'Z'):
        print("alphabet")
    else:
        print("special character;")
else:
    print("oversized character")
    
