"""Write a program to find and display the first non-repeating character in a user given string.
Display None if no non-repeating character found."""
str=input()
for i in str:
    if str.count(i)==1:
        print(i)
        break
else:
    print(None)
