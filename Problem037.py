from common_functions import primeSieve, isPrime

def isTruncatableRtoL(prime):

    while True:
        prime = prime/10
        if prime == 0:
            break
        if isPrime(prime):
            continue
        else:
            return False
    return True

def isTruncatableLtoR(prime):

    primeStr = str(prime)
    while len(primeStr)!=1:
        primeStr = primeStr[1:]
        
        if isPrime(int(primeStr)):
            continue
        else:
            return False
    return True

primes = primeSieve(1000000)
truncPrimeList = []

for prime in primes:
    if isTruncatableRtoL(prime) and isTruncatableLtoR(prime) and prime>10:
        
        print prime
        truncPrimeList.append(prime)

print len(truncPrimeList)
print sum(truncPrimeList)
