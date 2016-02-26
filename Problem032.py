def isPanDigitalSet(num1,num2,product):

    numString = str(num1)+str(num2)+str(product)
    if str(0) in set(numString):
        return False
    elif len(set(numString))==9:
        if len(numString) == len(set(numString)):
            return True
    else:
        return False



numberList = []
for i in range(2,90000):
    if i>90000/i:
        break
    for j in range(i+1,90000/i):
        if isPanDigitalSet(i,j,i*j):
            numberList.append(i*j)

numberSet = set(numberList)
numberList = list(numberSet)
print sum(numberList)
