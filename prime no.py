lowerrange=int(input("Enter lower range : "));
upperrange=int(input("Enter the upper range : "));
for num in range(lowerrange,upperrange):
    if num>1:
        for i in range(2,num):
            if (num % i) ==0:
                 break
        else:
                print(num)