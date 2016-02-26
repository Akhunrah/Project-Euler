

def powSum(number,power):
    numSum = 0
    while number!=0 or number%10!=0:
        numSum += pow(number%10,power)
        number = number/10
    return numSum

power = 5
maximum = (power+1)*pow(9,power)
numbers = []

for i in range(2,maximum+1):
    if i == powSum(i,power):
        numbers.append(i)
    

print sum(numbers)
    
