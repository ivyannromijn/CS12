def menu():
	print("======= OPTIONS =======")
	print("[1] Add a product")
	print("[2] View a product")
	print("[3] View all products")
	print("[4] Delete a product")
	print("[5] Delete all products")
	print("[6] exit")

	choice=int(input("Option:"))
	return choice

def addProduct(product):
	key=input("Enter product number:")
	if key in product.keys():
		print("Product already exists. \n")
		return product
	else:
		perproduct= {}

		brand=input("Enter product brand:")
		type=input("Enter product type:")
		weight=input("Enter product weight:")
		stock=input("Number of items in stock:")

		product[key]= perproduct
		perproduct["Brand:"]= brand
		perproduct["Type of product:"]= type
		perproduct["Weight of product:"]= weight
		perproduct["Number of stock:"]= stock

	return product

def viewProduct(product):
	if len(product)== 0:
		print("There are no items in the records yet.")
		return product
	else:
		print("Pick a product number from the following.")
		print()
		x=1
		for k in product:
			print("Product Number:", k)
			x= x+ 1
		print("========================")
		print()
		input_product = input("Choose a product number to view: ")
		print()
		if input_product in product.keys():
			print("\nProduct Number: \t", end=" ")
			print(input_product)
			
			print("Brand: \t\t\t", end=" ")
			print(product[input_product]["Brand:"])
			
			print("Type of Product : \t", end=" ")
			print(product[input_product]["Type of product:"])
			print("Weight : \t\t", end=" ")
			print(product[input_product]["Weight of product:"])
			print("No. of Items : \t\t", end=" ")
			print(product[input_product]["Number of stock:"], "pcs")
			print()
			return product
		else:
			print("Theres no product with that kind of number")
			print("Try again")
	
		

def viewAllProduct(product):
	if len(product)!=0:
		print("Products:")
		for k in product:
			print("("+k+")",product[k]["Brand:"],product[k]["Type of product:"],product[k]["Weight of product:"],"("+product[k]["Number of stock:"]+"pcs)")
		return product
	else:
		print("There are no items in the records yet.")
	


def deleteProduct(product):
	if len(product)!= 0:
		print("Pick a product number to delete.")
		print()
		x=1
		for k in product:
			print("Product Number:", k)
			x= x+ 1
		print("========================")
		print()
		
		input_product2 = input("\nEnter the product number: ")
		if input_product2 in product.keys():
			del product[input_product2]
			print("\nThe product was deleted successfully.")
			return product
		else:
			print("Theres no product with that number.")
			return product
	else:
		print("There are no records yet.")
		print("Add a product first.")

	

def deleteAllProduct(product):
	print("Are you sure you want to delete?")
	print("[1] Yes")
	print("[2] No")
	choice=int(input("Enter:"))
	if choice==1:
		if len(product) == 0:
			print("There are no records yet.")
			print("Add a product first.")
			menu()
		else:
			product={}
			print("All products are deleted")
			return product
	if choice==2:
		print("Delete unsuccessful")
		return product
		menu()
	else:
		print("Invalid option, try again")
		deleteAllProduct(product)
		return product
	
product={}

while True:
	c=menu()

	if c==1:
		product= addProduct(product)
	elif c==2:
		product= viewProduct(product)
	elif c==3:
		product= viewAllProduct(product)
	elif c==4:
		product=  deleteProduct(product)
	elif c==5:
		product= deleteAllProduct(product)
	elif c==6:
		print("=======END OF PROGRAM=======")
		break
	else:
		print("Invalid Option")

