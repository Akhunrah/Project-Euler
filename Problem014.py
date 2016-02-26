from common_functions import findLargerNumber

def collatzSequence(number):

    sequence = [number]
    nextNum = number
    while number!=1:
        if number%2==0:
            nextNum=number/2
        else:
            nextNum=3*number+1
        sequence.append(nextNum)
        number=nextNum

    return sequence

largest=1
numOfLargest=1

for i in range(2,1000000):
    length = len(collatzSequence(i))

    print i, length
    if length==findLargerNumber(length,largest):
        largest=length
        numOfLargest=i

print numOfLargest
    
