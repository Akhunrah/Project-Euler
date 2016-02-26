from common_functions import *
import time


factorials = []
for i in range(10):
    factorials.append(factorial(i))

def sumOfFactorials(num):
    result = 0
    while num!=0:
        result+=factorials[num%10]
        num = num/10
    return result


time0 = time.time()
finalNum = 0

for i in range(1000000):
    chain = []
    num = i
    while True:
        chain.append(num)
        num = sumOfFactorials(num)
        if num in chain:
            index = chain.index(num)
            break
    if len(chain)==60:
        finalNum+=1
        

print finalNum, time.time()-time0
