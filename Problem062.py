from common_functions import *

numL=[]
cubeL=[]
cubeDigitsL=[]
for i in range(300,10000):
    numL.append(i)
    cube=i*i*i
    cubeL.append(cube)
    cubeDigitsL.append(returnOrderedDigits(cube))

for i in range(len(cubeDigitsL)):
    cubeDigits=cubeDigitsL[i]
    if cubeDigitsL.count(cubeDigits)==5:
        indices=[i for i,x in enumerate(cubeDigitsL) if x ==cubeDigits]
        print indices
        for index in indices:
            print numL[index], cubeL[index]
        break
        
