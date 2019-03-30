#PythonAssignment4
#declare a global variable of list type.The list should be an empty list initially
myUniqueList=[]
print(type(myUniqueList))
def addItemToList(item):
	print("Item being added to list :", item)
	result=False
	itemFound=False
	#print(item in myUniqueList)
	if(item in myUniqueList):
		print("Item already Exists")
		itemFound=True
	if(itemFound==False):
		print("Item does not exists!!Adding new Item")
		myUniqueList.append(item)
		result=True
		return result
	else:
		print("Item already in myUniqueList")
		return result
#itemToadd=eval(input("Enter item to add to list : "))
itemToadd=10.5
print("Item Added :",addItemToList(itemToadd))
itemToadd='Pirple Learning Forum'
print("Item Added :",addItemToList(itemToadd))
itemToadd=10.5
print("Item Added :",addItemToList(itemToadd))
print(myUniqueList)