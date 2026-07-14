n=int(input("enter a number: "))
original = n
reverse = 0
while n>0:
    num = n%10
    reverse = reverse*10+num
    n=n//10
if original == reverse:
    print("yes")
else:
    print("no")