from common_functions import factorial

def sumOfDigitFactorials(num):

    numSum = 0
    while num!=0:
        numSum += factorial(num%10)
        num = num/10
    return numSum




for i in range(3,2000000):
    if sumOfDigitFactorials(i)==i:
        print i
