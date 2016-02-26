import math

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

print sum(primeSieve(2000000))

