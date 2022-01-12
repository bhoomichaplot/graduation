
# function to find ways to attend classes
def attend_class(n):
    k = 0
    if n >= 5:
        k = attend_class(n - 1) + attend_class(n - 2) + attend_class(n - 3) + attend_class(n - 4)
    elif n == 4:
        k = 15
    elif n == 3:
        k = 8
    elif n == 2:
        k = 4
    elif n == 1:
        k = 2
    return k
    
n =int(input("Enter Value "))
print("The number of ways to attend classes over N days is",attend_class(n))

# missing attend_class 
# 1 - f(n-1)/f(n)
graduation = attend_class(n)-attend_class(n-1)
print("The probability that you will miss your graduation ceremony is ",graduation,"/",attend_class(n))









