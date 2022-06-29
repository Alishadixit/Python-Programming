
def function1(a,b):
    sum=a + b
    return sum
c =function1(89,5)
print(c)


#Using doc string
def function2(a,b,c):
    """Here is the average of tw0 no"""
    average=(a+b)/2
    return average
#d=function2(100,8)
print(function2.__doc__)