from operator import attrgetter
class Product:
    def __init__(obj,pid,name,cost,brand,category,rating,discount):
        obj.pid=pid
        obj.name=name
        obj.cost=cost
        obj.brand=brand
        obj.category=category
        obj.rating=rating
        obj.discount=discount
        

class Choice:
    def __init__(obj, choice, reverse, inputt):
        obj.choice = choice
        obj.reverse = reverse
        obj.inputt = inputt
    

cList = []
cList.append(Choice("cost", False, 1))
cList.append(Choice("cost", True, 2))
cList.append(Choice("rating", True, 3))
cList.append(Choice("discount", False, 4))
cList.append(Choice("discount", True, 5))

        
pList = []
pList.append(Product("P001", "Mobile Phone", 120000, "Apple", "Electronics", 5, 50))
pList.append(Product("P002", "Television", 130000, "Onida", "Electronics", 3, 80))
pList.append(Product("P003", "Shirt", 1200, "Zara", "Clothing", 5, 20))

while True:
    print("1. Sort by cost (Low to High)")
    print("2.Sort by cost (High to Low)")
    print("3.Sort by rating")
    print("4.Sort by discount (Low to high)")
    print("5.Sort by discount (High to low)")
    c=int(input("Enter a choice\n"))
    pList.sort(key = attrgetter(cList[c-1].choice), reverse = cList[c-1].reverse)
    for obj in pList: 
        print( obj.pid, obj.name, obj.cost, obj.brand, obj.category, obj.rating, obj.discount, sep =' | ' )
        
    x = input("Do you want to continue? Y or N\n")
    
    if x == "N" or x == "n":
        break