#Write a program that takes an integer n and prints
#the first n prime integers. 

n=int(input("Enter how many prime integers you want:"))
primes=0
start=1

while primes!=n:
    if start>1:
        for divisors in range (2,start):
            if start%divisors==0:
                break
        else:
            print(start)
            primes=primes+1
            
    start=start+1
#end of program