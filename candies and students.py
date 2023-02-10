n = int(input("enter number of students;"))
c = int(input("enter the number of candies;"))
s = 0
for i in range(1, n + 1):
    a = int(input("enter candies for " + str(i) + " student"))
    s = s + a
if s >= c:
    print("no")
else:
    print("yes")
