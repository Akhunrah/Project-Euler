numbers=[]
numRange=range(2,101)

for a in numRange:
    for b in numRange:
        numbers.append(pow(a,b))

numbersSet = set(numbers)
numbers = list(numbersSet)
numbers.sort()

print len(numbers)
