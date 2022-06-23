'''num = int(input("ENTER A NUMBER (0..999) :"))
if num<0:
    print("INVALID ENTRY")
elif num<10:
    print(" SINGLE DIGIT ENTERED")
elif num<100:
    print("DOUBLE DIGIT ENTERED")
elif num<=999:
    print("TRIPLE DIGIT ENTERED")
else:
    print("invalid data entered")'''
# above program using if else only.
num =int(input("ENTER A NO (0..999) : "))
if num<0 or num> 999 :
    print("you have entered invalid data")
else:
    if num<10:
       print("you have entered single digit data")
    else:
      if num<100:
        print("you have entered double digit data")
      else:
        print (" you have entered triple digit data")


