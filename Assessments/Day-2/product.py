choice = int(input("1.Sort by Cost (L-H)\n"
                   "2.Sort by Cost (H-L)\n"
                   "3.Sort by Rating\n"
                   "4.Sort by Discount (L-H)\n"
                   "5.Sort by Discount (H-L)\n"))



products =[
    {"Pid":1,"Name":"Vivo V9","Cost":"23999","Brand":"Vivo","Category":"Mobiles","Rating":4,"Discount":39},
    {"Pid":2,"Name":"Oppo F11","Cost":"26999","Brand":"Oppo","Category":"Mobiles","Rating":4,"Discount":23},
    {"Pid":3,"Name":"One+ 5T","Cost":"34999","Brand":"Oneplus","Category":"Mobiles","Rating":4,"Discount":19},
    {"Pid":4,"Name":"Nav tv","Cost":"69999","Brand":"Nav","Category":"Home appliances","Rating":5,"Discount":9},
    {"Pid":5,"Name":"Elitebook G5","Cost":"100500","Brand":"HP","Category":"Laptop","Rating":5,"Discount":20},
    {"Pid":6,"Name":"Smart LED T.V","Cost":"59999","Brand":"Samsung","Category":"Home appliances","Rating":4,"Discount":30},
    {"Pid":7,"Name":"Fullyloaded machine","Cost":"45999","Brand":"L.G","Category":"Home appliances","Rating":5,"Discount":24},
    {"Pid":8,"Name":"Dell 4535","Cost":"79999","Brand":"Dell","Category":"Laptop","Rating":3,"Discount":35},
    {"Pid":9,"Name":"Lenovo Flip Book","Cost":"85699","Brand":"Lenovo","Category":"Laptop","Rating":2,"Discount":65},
    {"Pid":10,"Name":"Asus a8","Cost":"36999","Brand":"Asus","Category":"Laptop","Rating":1,"Discount":55}]


print (type(products))

#sort
sorttype =[["Cost",False],["Cost",True],["Rating",True],["Discount",False],["Discount",True]]

products.sort(key = lambda ele: ele[sorttype[choice-1][0]], reverse=sorttype[choice-1][1])

print("Name"          ,"Cost"    ,"Brand"   ,"Category"  ,"Rating" ,"Discount",sep="\t\t")
for i in products:
    print(i["Name"],"         ",i["Cost"],"     ",i["Brand"],"      ",i["Category"],"             ",i["Rating"],"     ",i["Discount"],sep="\t")	
		
#filter
choice2 = int(input("1.Filter by Name\n"
                    "2.Filter by Brand\n"
                    "3.Filter by Category\n"))
filtertype =["Name","Brand","Category"]
string = input("Enter : ")
newobj = filter(lambda ele: ele[filtertype[choice2-1]] == string,products)
print("Name    Cost    Brand   Category    Rating  Discount")
for i in newobj:
    print(i["Name"],"    ",i["Cost"],"    ",i["Brand"],"    ",i["Category"],"    ",i["Rating"],"    ",i["Discount"],sep="\t")
	



		



