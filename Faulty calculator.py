a=int(input("enter your number"))
b=int(input("enter second num"))
c=input("enter your operator Addition +,Subbtraction -,Multiplication *,Divison /")

if a==45 and b==3 and c=="*":
    print("ans is 555")
elif a==56 and b==9 and c=="+":
    print("ans is 77")
elif a==56 and b==6 and c=="/":
    print("ans is 4")
elif c=="+":
    plus = a + b
    print(plus)
elif c=="-":
    sub=a -b
    print(sub)
elif c=="*":
    multiply=a*b
    print(multiply)
elif c=="/":
    divide=a /b
    print(divide)

else:
    print("")

