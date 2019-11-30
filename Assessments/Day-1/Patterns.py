print("1")
num=int(input("Enter a number: "))
for i in range(0,num+1):
    for j in range(0,i):
        print("*" ,end=" ")
    print()
print("=============================")
print("2")
n=4
while n>0:
    print(" "*(n-1)," *"*(4-n))
    n-=1
print(" ")
print("=============================")
print("3")
n=4
while n>0:
    print(" "*(4-n),"*"*(n-1))
    n-=1
print()
print("=============================")  
print("4")
n=4
while n>0:
    print("*"*(n-1),"  "*(4-n))
    n-=1
print()
print("=============================")  
print("5")
n=4
while n>0:
    print(" "*(n-1),"*"*(4-n))
    n-=1
print()
print("=============================")  
print("6")
word="python"
for i in range(0,6):
    print(" "*(6-(i+1)),word[0:(6-(6-(i+1)))])           
print()
print("=============================") 
num=int(input("Enter number for factorial: ") )
for i in range(1,num):
    print(i,"*",end="")
print(num)
print("=============================") 
num=int(input("Enter number for fibbonacci: ") )
n1=0
n2=1
for i in range(1,num+2):
    print(n1+n2,end=" ")
    n3=n1+n2
    n1=n2
    n2=n3