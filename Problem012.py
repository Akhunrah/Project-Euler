from common_functions import findDivisors

length = 1
i = 1

while True:
    i+=1
    triangleNum=sum(range(i))
    length = len(findDivisors(triangleNum))

    if length>500:
        print triangleNum, length
        break
    
