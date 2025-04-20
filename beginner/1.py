obj = []	
def main_menu():
	numAdd = 0
	numRemove = 0
	T = True
	def add(i):
		obj.append(i)
		print(obj)
		
	def remove(i):
		obj.remove(i)
		print(obj)
	while T:
		number = int(input("select : "))
		if number==0:
			print("select : ",number,"Add : ",numAdd,"Remove : ",numRemove)
			break
		elif number==1:
			while T:
				y = str(input("Add to list yes/no : "))			
				if y=="yes":
					numAdd += 1
					x = str(add(input("put to list : " )))
				elif y=="no":
					print("select : ",number,"Add : ",numAdd,"Remove : ",numRemove)					
					break
			continue
					
		elif number==2:
			while T:
				y = str(input("Delete to list yes/no : "))		
				if y=="yes":
					numRemove += 1
					x = str(remove(input("remove to list : " )))
				elif y=="no":
					print("select : ",number,"Add : ",numAdd,					"Remove : ",numRemove)
					break
			continue
	return
		
main_menu()
    