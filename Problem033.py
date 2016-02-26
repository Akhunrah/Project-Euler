from common_functions import gcd

def hasCommonNonZeroDigit(num1,num2):

    num1FirstDigit = num1/10
    num1SecondDigit = num1%10
    num2FirstDigit = num2/10
    num2SecondDigit = num2%10

    if num1FirstDigit == num2FirstDigit or num1FirstDigit == num2SecondDigit:
        if num1FirstDigit==0:
            return False
        else:
            return True
    elif num1SecondDigit == num2FirstDigit or num1SecondDigit == num2SecondDigit:
        if num1SecondDigit==0:
            return False
        else:
            return True
    else:
        return False

def removeCommonNonZeroDigit(num1,num2):
    num1FirstDigit = num1/10
    num1SecondDigit = num1%10
    num2FirstDigit = num2/10
    num2SecondDigit = num2%10

    if num1FirstDigit == num2FirstDigit:
        return num1SecondDigit,num2SecondDigit
    elif num1FirstDigit == num2SecondDigit:
        return num1SecondDigit, num2FirstDigit
    elif num1SecondDigit == num2FirstDigit:
        return num1FirstDigit, num2SecondDigit
    elif num1SecondDigit == num2SecondDigit:
        return num1FirstDigit, num2FirstDigit

def lowestTermsFraction(num,den):
    
    d = gcd(den,num)
    return num/d, den/d
    

num = 1
den = 1

for i in range(10,99):
    for j in range(i+1,100):
        if hasCommonNonZeroDigit(i,j):
            num1,den1 = removeCommonNonZeroDigit(i,j)
            num1,den1 = lowestTermsFraction(num1,den1)
            num2,den2 = lowestTermsFraction(i,j)
            if num1 == num2 and den1 == den2:
                print i,j,num1,den1
                num = num1*num
                den = den1*den

num, den = lowestTermsFraction(num,den)

print num, den


