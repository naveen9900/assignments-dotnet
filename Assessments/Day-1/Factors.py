
num=int(input("Enter a number "))
i=1
count=0

sum=0
while i<=num/2:
    if(num%i==0):
        print(i," is a factor")
        count+=1
        sum=sum+i
    i+=1
print("Count ",count)
print("Sum ",sum)