from common_functions import primeSieve, isPrime

# Looking for a and b such that f(n)=n*n +a*n +b produces a prime,
# beginning with n=0, with the condition that the magnitudes of a and b
# are both less than 1000.
# For n=0, f(n)=b, which means b must be prime:
maxRange = 1000
bList = primeSieve(maxRange)



# The variable largest stores the largest number of primes produced.
# The variable ab stores the product of a and b that produced largest.
largest = 0 
ab = 0

for b in bList:
    
    for a in range(-maxRange,maxRange+1):
        numOfPrimes=1
        n=1
        while True:
            possiblePrime = n*n+a*n+b
            if isPrime(possiblePrime):
                numOfPrimes+=1
            else:
                largest = max(largest,numOfPrimes)
                if largest == numOfPrimes:
                    ab=a*b
                break
            n+=1

print ab
                
