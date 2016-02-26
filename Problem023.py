from common_functions import findProperDivisors

abundantNums=[]
maxInt=28123

for i in range(1,maxInt+1):
    if sum(findProperDivisors(i))>i:
        abundantNums.append(i)

abundantSums=[]

for i in range(len(abundantNums)):
    for j in range(i,len(abundantNums)):
        number=abundantNums[i]+abundantNums[j]
        if number<=maxInt:
            abundantSums.append(number)

numbers=range(1,maxInt+1)
numbersSet=set(numbers)
abundantSumsSet=set(abundantSums)
numbersSet=numbersSet-abundantSumsSet
print sum(numbersSet)
    
