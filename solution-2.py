
import numpy as np


# function to find ways to attend classes
def attend_class(n):
    # create array
    num = np.full([n],int(0))    

    num[0] = 2
    num[1] = 4
    num[2] = 8
    num[3] = 15
    if n == 0:
        return num[0]
    elif n==1:
        return num[1]
    elif n==2:
        return num[2]
    elif n==3:
        return num[3]
    else:   
        for i in range(4,n):
            num[i] = num[i - 1] + num[i - 2] + num[i - 3] + num[i - 4]
            pass

        return num[n-1]

n =int(input("Enter Value "))
print("The number of ways to attend classes over N days is",attend_class(n))

# # missing attend_class 
# # 1 - f(n-1)/f(n)
graduation = attend_class(n)-attend_class(n-1)
print("The probability that you will miss your graduation ceremony is ",graduation,"/",attend_class(n))