#Write a program that prints the largest odd number given three number.
x=int(input("Enter first number:"))
y=int(input("Enter second number:"))
z=int(input("Enter third number:"))

if x%2!=0 and y%2!=0 and z%2!=0: #if all are odd
	if x>y and  x>z:
		print("The largest odd number is", x)
	else:
		if y>z and y>x:
			print("The largest odd number is", y)
		else:
			if z>x and z>y:
				print("The  largest odd number is", z)
#if 2 numbers are odd
else:
	if x%2!=0 and y%2!=0:
		if x>y:
			print("The largest odd number is", x)
		else:
		 	print("The largest odd number is", y)
	else:
		if y%2!=0 and z%2!=0:
			if y>z:
				print("The largest  odd number is", y)
			else:
				print("The largest odd number is", z)
		else:
			if x%2!=0 and z%2!=0:
				if x>z:
					print("The largest odd number is", x)
				else:
					print("The largest odd number is", z)
					#if only one number
			else:
				if x%2!=0 and y%2==0 and z%2==0:
					print("The largest odd number is", x)
				else:
					if x%2==0 and y%2!=0 and z%2==0:
						print("The largest odd number is", y)
					else:
						if x%2==0 and y%2==0 and z%2!=0:
							print("The largest odd number is", z)
						else: #no odd number
							if x%2==0 and y%2==0 and z%2==0:
								print("There is no odd number")

#end of program
#avoided using elsif because it is easier for me  to see the conditions. Thank you!