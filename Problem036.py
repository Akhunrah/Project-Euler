from common_functions import isPalindromicNumber,isPalindromicString


##for i in range(600):
##    iBinary = convertDecimalToBinary
##
##    if isPalindromicNumber(i) and isPalindromicString(iBinary):
##        print i


numSum = 0
for i in range(1000000):
     if isPalindromicNumber(i) and isPalindromicString(bin(i)[2::1]):
         numSum+=i
print numSum
