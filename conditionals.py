'''Q- driving eligiblity'''

print("ENTER YOUR AGE");
age: int=int(input());
if age > 18 and age<=100:
    print("YOU ARE ELIGIBLE FOR DRIVING")
elif age==18:
    print("WE WILL CONSIDER YOU")
else:
    print("YOU ARE  NOT ELIGIBLE")
