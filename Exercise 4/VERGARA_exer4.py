


#create a program that asks the user for two positive integers
# x and y, and performs the following operations on those integers

    # Addition (x+y); 
    # subtraction (x-y);
    # multiplication (using repeated addition)
    # integer division ( using repeated subtraction)
    # exponentation ( using repeated multiplication)

x=int(input("Enter 1st integer:"))
y=int(input("Enter 2nd integer:"))
print()
print()



def menu():
	print("******* OPTIONS *******")
	print("[1] Addition")
	print("[2] Subtraction")
	print("[3] Multiplication")
	print("[4] Division")
	print("[5] Exponentation")
	print("[0] exit")

menu()
option=int(input("Enter your option:"))

while option !=0:
	if option ==1:
		sum= x+y
		print("You've chosen addition, the sum is", sum)
	elif option==2:
		difference= x-y
		print("You've chosen subtraction, the difference is", difference)
	elif option ==3:
		product=0
		count=0
		while count!=y:
			product=product+x
			count=count+1
		print("You've chosen multiplication, the product is", product)
	elif option ==4:
		if x>y:
			def quo(x):
				count1=0
				while x>=1:
					x=x-y
					count1=count1 +1
				return count1
			quotient= quo(x)
			print ("You've entered division, the quotient is", quotient)
		else:
			def quo2(y):
				count2=0
				while y>=1:
					y=y-x
					count2=count2+1
				return count2
			quotient2= quo2(y)
			print ("You've entered division, the quotient is", quotient2)
	elif option ==5:
		count3= 1
		answer=1
		while count3!=y+1:
			answer=answer* x
			count3= count3 +1
		print("You've chosen exponentation, the answer is", answer)
	else:
		print("Invalid option, try again")

	print()
	menu()
	option=int(input("Enter another option or exit:"))

print("End of exercise 4")
  

