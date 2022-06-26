#AREA OF TRIANGLE


a=float(input("Enter Your first Side"))
b=float(input("Enter Your second Side"))
c=float(input("Enter your third side"))
sum  =(a+b+c) / 2
area = (sum*(sum-a)*(sum-b)*(sum-c))**0.5
print('The area of the triangle is %0.2f' %area)



