import math    
        


def gcd(m,n):

    if m == 0:
        return n
    elif n == 0:
        return m
    
    if m%n == 0:
        return n
    else:
        return gcd(n,m%n)    



def sieveOfEratosthenes(maximum):

    numbers = [2]
    numbers.extend(set(range(3,maximum+1,2)))
    

    divisorIndex = 1
    
    while True:
        if divisorIndex == len(numbers):
            break
        
        numberIndex = divisorIndex+1
        divisor = numbers[divisorIndex]
        while True:

            if numberIndex == len(numbers):
                break
            number=numbers[numberIndex]
            
            if number%divisor==0:
                numbers.remove(number)
            else:
                numberIndex+=1

        divisorIndex+=1

    return list(numbers)


        

def primeSieve(number):
    # Returns a list of primes using the Sieve of Eratosthenes
    numbers = range(3,number+1)
    primes = [2]
    primeBool=True

    for number in numbers:
        primeBool=True
        for prime in primes:
            if prime>math.sqrt(number):
                break
            if number%prime==0:
                primeBool=False
        if primeBool:
            primes.append(number)
    return primes




def includeNextPrime(primes):

    number = max(primes)
    while True:
        number +=1
        primeBool = True
        for prime in primes:
            if prime>math.sqrt(number):
                break
            if number%prime==0:
                primeBool = False
        if primeBool:
            primes.append(number)
            break

    return primes






def isPrime(number):
    if number<=1: return False
    if number==2: return True
    if number%2==0: return False
    if number<9: return True
    if number%3 == 0: return False

    divisor=5
    while divisor*divisor<=number:
        if number%divisor==0: return False
        if number%(divisor+2)==0: return False
        divisor+=6
    return True




def findDivisors(number):
    # Finds all divisors of number, stores them in a list, sorts them,
    # and returns the list.

    maximum=int(math.sqrt(number))
    divisors=[]
    for i in range(1,maximum+1):
        if number%i==0:
            divisors.append(i)
            divisors.append(number/i)

    divisorSet=set(divisors)
    divisors = list(divisorSet)
    divisors.sort()
    return divisors




def findProperDivisors(number):
    # Returns a sorted list of proper divisors of number.
    divisors = findDivisors(number)
    divisors.remove(number)
    divisors.sort()
    return divisors





def factorial(number):
    # Returns the factorial of a number.
    if number == 0:
        return 1
    elif number==1:
        return 1
    else:
        return number*factorial(number-1)


def combinatorial(n,r):
    return factorial(n)/(factorial(r)*factorial(n-r))



def returnDigitsOf(num):
    digits = []
    while num!=0:
        digits.insert(0,num%10)
        num=num/10
    return digits        



def digitSum(number):
    # Sums up the digits in number.

    digitSum = 0
    while number!=0:
        digitSum+=number%10
        number = number/10
    return digitSum

def fibonacci(i):
    # Returns the ith fibonacci number.
    if i==0:
        return 1
    elif i==1:
        return 1
    else:
        return fibonacci(i-1)+fibonacci(i-2)

    
    
def isPalindromicNumber(number):
    number1=number
    number2=0
    while number!=0:
        number2=10*number2+number%10
        number=number/10
    if number1==number2:
        return True
    else:
        return False
    


def isPalindromicString(string):
    
    
    if string == string[::-1]:
        return True
    else:
        return False


def returnOrderedDigits(number):

    digitList=[]
    while number!=0:
        digitList.append(number%10)
        number=number/10
    digitList.sort()
    digitString=''
    for digit in digitList:
        digitString+=str(digit)
    return digitString





def integerLength(integer):
    return len(str(integer))




def continuedFractionSQRT(x,size):
    m=1
    while True:
        if m*m==x:
            return [m,[]]
        elif m*m<x:
            m+=1
        else:
            m-=1
            break
    termL=[]
    #First term:
    q=x-m*m
    a=(2*m)/q
    p=a*q-m
    termL.append(a)
    for i in range(size):
        if (x-p*p)%q==0:
            qNew=(x-p*p)/q
            aNew=(m+p)/qNew
            pNew=qNew*aNew-p
            termL.append(aNew)
            a=aNew
            p=pNew
            q=qNew
            
        
    return [m,termL]




def findPeriod(intList):

    if len(intList)==0:
        return 0
    
    
    period=1
    flag=False
    while flag==False:
        seqL=[]
        i=0
        while (i+1)*period<len(intList):
            seqL.append(intList[i*period:(i+1)*period])
            i+=1
        if seqL.count(seqL[0])==len(seqL):
            return period
        period+=1


def convergentFraction(fraction):
    m=fraction[0]
    sequence = fraction[1][::-1]
    p=1
    q=sequence[0]
    for i in range(1,len(sequence)):
        pNew=q
        qNew=q*sequence[i]+p
        p=pNew
        q=qNew
    return p+m*q,q




def isSquare(number):
    i=0
    while i*i<number:
        i+=1
        if i*i==number:
            return True
    return False




def totient(number):
    numL=[]
    for i in range(1,number):
        if gcd(i,number)==1:
            numL.append(i)
    return len(numL)




def reducedFraction(numL):
    n = numL[0]
    d = numL[1]
    GCD = gcd(n,d)
    return [n/GCD,d/GCD]
    
    
