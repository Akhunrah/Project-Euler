from common_functions import findDivisors

def findProperDivisors(number):
    divisors = findDivisors(number)
    divisors.remove(number)
    divisors.sort()
    return divisors

amicables=[]
maxNum=10000

for i in range(10,maxNum+1):
    num1=i
    num1Div = findProperDivisors(num1)
    
    num2=sum(num1Div)
    num2Div = findProperDivisors(num2)
    if num1 == sum(num2Div) and num1!=num2 and num1<maxNum+1 and num2<maxNum+1:
        amicables.append(num1)
        amicables.append(num2)

print amicables

amicablesSet = set(amicables)
amicables = list(amicablesSet)
amicables.sort()

print amicables
print sum(amicables)

    
    
