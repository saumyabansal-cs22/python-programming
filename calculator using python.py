print("************Calculator**************")
print("1.Additon")
print("2.Subtraction")
print("3.Division")
print("4.Multiplication")
a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
c=input("Enter the operation:")

match(c):
    case '+':
        print(a+b)
    case '-':
        print(a-b)
    case '*':
        print(a*b)
    case '/':
        print(a/b)
    case '//':
        print(a//b)


    
    