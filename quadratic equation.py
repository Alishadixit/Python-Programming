import cmath
a=int(input("Enter value of a :"))
b=int(input("Enter the value of b :"))
c=int(input("Enter the value of c "))
disc=(b**2) - (4*a*c)
sol1 = (-b-cmath.sqrt(disc))/(2*a)
sol2 = (-b+cmath.sqrt(disc)/(2*a))
if disc>0:
    print("roots are real and different")
    print(sol1,sol2)
elif disc==0:
    print ("both roots are real")
    print(sol1, sol2, sep="and")
else:
  print("roots are complex")
  print(sol1,sol2,sep="and")