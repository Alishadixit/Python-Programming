#for loop
for  i in range(1,10,2):
    print(i)
#while loop
i=1
while (i <= 10):
    print(i)
    i=i+1

#break and continue
i=1
while (i<=10):
    print(i)
    if(i==5):
        break
    i=i+1
#continue
i=1
while (i<=10):
    i = i + 1
    if(i==5):
        continue
    print(i)
