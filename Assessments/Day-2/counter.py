print("===================================== Using non-local-print number of function calls")
def outer():
    count=0
    def inner():
        nonlocal count
        count+=1
        print(count)
    return inner
    
hello=outer()
print(type(hello))
hello()#lexical referencing of the function to the count variable makes the value of count persist
hello()
hi=outer()
hello()
hello()
hi()
hi()