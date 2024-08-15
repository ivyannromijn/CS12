def user_input():
    x=int(input("Enter 1st integer:"))
    y=int(input("Enter 2nd integer:"))
    return x,y


def multiply(x,y):
    if y==0:
        return 0
    else:
        return (x+multiply(x, y-1))


def divide(x,y):
    if x == 0:
        return 0

    if x < y:
        print("Remainder is", x)
        return 0

    return 1 + (divide(x - y,y))



def menu():
    print("========EXER 08=========")
    print("[1] Multiplication")
    print("[2] Division")
    print("[0] exit")
    print("========================")
    choice= int(input("Option:"))
    return choice


while True:
   choice=menu()

   if choice ==  1:
       x,y= user_input()
       print("x*y= \t", multiply(x,y))
   elif choice==2:
       x,y= user_input()
       if y==0:
           print("Math error")
       else:
           print("x/y= \t", divide(x,y))
   elif choice==0:
       print("=======END OF PROGRAM========")
       break
   else:
       print("Invalid option")
       
