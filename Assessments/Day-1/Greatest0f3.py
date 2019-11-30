a=input("Enter number: ")
b=input("Enter number: ")
c=input("Enter number: ")

if a>b:
    if a>c:
        print(a," is greatest")
    else:
        print(c," is greatest")
elif b>a:
       if b>c:
        print(b," is greatest")
       else:
        print(b," is greatest")
else:
    print(c," is greatest")