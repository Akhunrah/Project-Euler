from common_functions import isPrime2,primeSieve

def numOfUniquePrimeDivisors(number, primes):

    index = 0
    divisors = []
    while number!=1:

        prime = primes[index]
        if number%prime == 0:
            number = number/prime
            divisors.append(prime)
        else:
            index+=1
    return len(set(divisors))

        
        

maximum = 1000000
primes = primeSieve(maximum)

numOfDivisors = 4
numWithCond = 0
number = 0

while numWithCond!=numOfDivisors:
    
    number+=1
    
    if numOfUniquePrimeDivisors(number,primes)==numOfDivisors:
        numWithCond+=1
    else:
        numWithCond = 0

print number
    
    
    
