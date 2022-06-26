num=int(input("Enter Your Number: "))
sum=0
i=1
while i<num:
    if num%i==0:
        sum=sum+i
    i=i+1
if num==sum:
    print("no is perfect")
else:
    print("no is not perfect")