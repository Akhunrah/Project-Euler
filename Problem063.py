import math
from common_functions import *

integerL=[]
power=1
while True:
    i=1
    currentLength=len(integerL)
    
    while True:
        integer=int(pow(i,power))
        if integerLength(integer)==power:
            integerL.append(integer)
            
        elif integerLength(integer)>power:
            break
        i+=1
        
    
    
    if currentLength!=len(integerL):
        power+=1
    else:
        break

print integerL, len(integerL)
