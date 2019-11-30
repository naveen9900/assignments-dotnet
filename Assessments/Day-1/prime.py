num=int(input("Enter a number "))
i=2
count=0
#sum=0
while i<=num/2:
    if(num%i==0):
       
        break
    else:
        count+=1
    i+=1
    if(count!=0):
        print("Not prime")
    else:
        print("Prime")