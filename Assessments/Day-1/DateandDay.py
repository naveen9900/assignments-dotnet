a=int(input("Enter date"))
rem=a%7
li=["Thurs","Friday","Sat","Sun","Mon","Tue","Wed"]
if (a>=1) and (a<=30):
    print(li[rem])
else:
    print("Invalid")