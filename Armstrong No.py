num=int(input("Enter you digit"))
temp=num
sum=0
digit=0
while temp>0:
    digit=temp%10
    sum=sum+digit**3
    temp=temp//10
if num==sum:
   print(num,"number is armstrong")
else:
   print((num,"no is not armstrong"))