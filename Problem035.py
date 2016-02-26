from common_functions import primeSieve

def isPrime(prime,primes):
    for divisor in primes:
        if prime == divisor:
            break
        elif prime%divisor == 0:
            return False
        else:
            continue
    return True

def isCircularPrime(prime,primes):

    length = len(str(prime))
    for i in range(length):
        prime = (prime%10)*pow(10,length-1)+prime/10
        if isPrime(prime,primes):
            continue
        else:
            return False
    return True
    

maximum = 1000000
num = 1 #for the prime of 2
primes = primeSieve(maximum)

print len(primes)

for prime in primes:

    if '0' in list(str(prime)) or '2' in list(str(prime)) or '4' in list(str(prime)) or  '6' in list(str(prime)) or  '8' in list(str(prime)) :
        continue
    else:
        if isCircularPrime(prime,primes):
            print prime
            num+=1

print num



