


primes = [2]
number=3
while len(primes)<10001:
    isPrime=True
    for prime in primes:
        if number%prime == 0:
            isPrime=False
            number+=1
            break
    if isPrime:
        primes.append(number)
    
        
length=len(primes)
print length
print primes[length-1]

