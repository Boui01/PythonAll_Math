import os
obj = ["A","A","B","C"]
def add(Y):
	x = str(input("put to list : ")) 
	Y.append(x)
	print(obj)
def remove(Y):
	x = str(input("remove to list : " ))
	Y.remove(x)
	print(obj)
def pop(Y):
	x = input("Pop to list : " )
	Y.pop(int(x))
def insert(Y):
	x = str(input("Position to list : " ))
	y = str(input("Insert to list : " ))
	Y.insert(int(x),y)
	print(obj)
def find(Y):
	x = str(input("Find to list : " ))
	result = Y.index(x)
	print(result)
def count(Y):
	x = str(input("Count to list : " ))
	result = Y.count(x)
	print(x," has ",result)
def sort():
	obj.sort()
def Clear():
	obj.clear()
def xdel(Y):
	x = str(input("Xdel to list : " ))
	z = Y.count(x)
	#result = [ele for ele in Y if ele != x]
	for i in range(z):
		Y.remove(x)
	print(x," has ",Y)
def replace(Y):
	i = str(input("original to list : " ))
	j = str(input("change to list : " ))
	x = Y.index(i)
	Y.remove(i),Y.insert(x,j)
	print(obj)
def Main():
	numAdd = 0
	numRemove = 0
	numPop = 0
	numInsert = 0
	numFind = 0
	numCount = 0 
	numSort = 0
	numClear = 0
	numXdel = 0
	numReplace = 0
	T = True
	def Print():
		print(obj,"\nselect : ",number,"Add : ",numAdd,"Remove : ",numRemove,"Pop : ",\
		numPop,"Insert : ",numInsert,"Find : ",numFind,"Count : ",numCount,"Sort : ",numSort,\
		"Clear : ",numClear,"Xdel : ",numXdel,"Replace : ",numReplace)
		print("------------------------------------------------------------------------\n")
	while T:
		number = int(input("Exit = 0 Add = 1 Remove = 2 Pop = 3 Insert = 4 Find = 5 Count = 6  Sort = 7 Clear = 8 Xdel = 9 Replace = 10 \nselect : "))
		if number==0:
			os.system('cls')
			Print()
			break
		elif number==1:
			while T:
				y = str(input("Add to list yes/no : "))			
				if y=="yes":
					numAdd += 1
					add(obj)
				elif y=="no":
					os.system('cls')
					Print()				
					break
			continue					
		elif number==2:
			while T:
				y = str(input("Delete to list yes/no : "))		
				if y=="yes":
					numRemove += 1
					remove(obj)
				elif y=="no":
					os.system('cls')
					Print()
					break
			continue
		elif number==3:
			while T:
				y = str(input("Pop to list yes/no : "))		
				if y=="yes":
					numPop += 1
					pop(obj)
				elif y=="no":
					os.system('cls')
					Print()
					break
			continue	
		elif number==4:
			while T:
				y = str(input("Insert to list yes/no : "))		
				if y=="yes":
					numInsert += 1
					insert(obj)
				elif y=="no":
					os.system('cls')
					Print()
					break
			continue
		elif number==5:
			while T:
				y = str(input("Find to list yes/no : "))		
				if y=="yes":
					numFind += 1
					find(obj)
				elif y=="no":
					os.system('cls')
					Print()
					break
			continue
		elif number==6:
			while T:
				y = str(input("Count to list yes/no : "))		
				if y=="yes":
					numCount += 1 
					count(obj)
				elif y=="no":
					os.system('cls')
					Print()
					break
			continue
		elif number==7:
			while T:
				numSort += 1
				sort()
				os.system('cls')
				Print()
				break
			continue
		elif number==8:
			while T:
				numClear += 1				
				Clear()	
				os.system('cls')
				Print()
				break
			continue
		elif number==9:
			while T:
				y = str(input("Xdel to list yes/no : "))		
				if y=="yes":
					numXdel += 1 
					xdel(obj)
				elif y=="no":
					os.system('cls')
					Print()
					break
			continue
		elif number==10:
			while T:
				y = str(input("Replace to list yes/no : "))		
				if y=="yes":
					numReplace += 1 
					replace(obj)
				elif y=="no":
					os.system('cls')
					Print()
					break
			continue
Main()
