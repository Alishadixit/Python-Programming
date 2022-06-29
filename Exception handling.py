print("Enter your number")
num1=(input())
print("Enter your number")
num2=(input())
try:
    print("The sum of no is :",
          int(num1) + int(num2))
except Exception as e:
    print(e)
    print("this line is very important")

