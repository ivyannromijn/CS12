#Write a program that a student can use to compute  their general weighted average (GWA) 
#for  1 semester (5 subjects)
print("Compute GWA")


a=float(input("Enter your grade in first subject:"))
a1=int(input("How many  units in this subject?"))
b=float(input("Enter your grade in second subject:"))
b1=int(input("How many  units in this subject?"))
c=float(input("Enter your grade in third subject:"))
c1=int(input("How many  units in this subject?"))
d=float(input("Enter your grade in fourth subject:"))
d1=int(input("How many  units in this subject?"))
e=float(input("Enter your grade in fifth subject:"))
e1=int(input("How many  units in this subject?"))


sub1=a*a1
sub2=b*b1
sub3=c*c1
sub4=d*d1
sub5=e*e1
sumofgrade=sub1+sub2+sub3+sub4+sub5
totalunits=a1+b1+c1+d1+e1

GWA=sumofgrade/totalunits
print("Your GWA is", GWA)
#END

