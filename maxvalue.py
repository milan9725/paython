a=int(input("enter a:"))
b=int(input("enter b:"))
c=int(input("enter c:"))

if a>b:
    if a>c:
        print("a is max value")
    else:
        print("c is max value")
elif b>c:
    print("b is max value")
else:
    print("c is max value")