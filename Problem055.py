from common_functions import isPalindromicNumber

def reverseDigits(number):
    number2=0
    while number!=0:
        number2=10*number2+number%10
        number=number/10

    return number2


def isLychrel(number):
    n=0
    while n<=50:
        number+=reverseDigits(number)
        n+=1
        if isPalindromicNumber(number):
            return True            
    return False


numOfLychrel = 0
for i in range(1,10001):
    if isLychrel(i)==False:
        numOfLychrel+=1

print numOfLychrel
        
    
        
