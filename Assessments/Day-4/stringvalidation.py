def demo(a):

    def inner(*args, **kwargs):
        value = False
        if len(args) > 0 and len(kwargs) > 0:
            print("inside both")
            if check(args, False) and check(kwargs, True):
                value = True
        elif len(args) > 0:
            print("inside args")
            if check(args, False):
                value = True
        elif len(kwargs) > 0:
            print("inside kwargs")
            if check(kwargs, True):
                print("inside  check")
                value = True
        if value:
            print ("Yes")
            a(*args, **kwargs)
        else:
            print("No")
    return inner

def check(args, isKwargs):
    value = False
    o = args.values() if isKwargs else args
    for val in o:
        if isinstance(val, str):
            value = True
        else:
            value = False
            break
    return value

@demo
def sayhi(name):
    print ("Hi " + name)

@demo
def sayhello(name1, name2):
    print ("Hello All " + name1 + " " + name2)

sayhi("Hi")
sayhello(name1="Aatisha", name2=1)