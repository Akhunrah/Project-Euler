
    
def findPrimes(number):
    #Finds primes below number using sieve of Eratosthenes
    primes = range(2,number+1)
    index1 = 0
    index2 = 1
    while index2!=len(primes):
        index1=0
        while index1<index2:
            divisor = primes[index1]
            prime = primes[index2]
            if prime%divisor == 0:
                primes.remove(prime)
                index2-=1
            else:
                index1+=1
        index2+=1
    return primes

def gcd(num1,num2):
    if(num1%num2==0):
        return num2
    else:
        return gcd(num2,num1%num2)

def findSmallestMultiple(number):
    factors = range(1,number+1)
    multiple = number
    for factor in factors:
        if gcd(multiple,factor)!=factor:
            multiple=multiple*factor/gcd(multiple,factor)
    print multiple

findSmallestMultiple(20)
            


            
        

