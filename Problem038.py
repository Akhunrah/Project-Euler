def isPandigital(numString):

    

    if '0' in set(numString):
        return False
    elif len(numString) == 9 and len(set(numString))==9:
        return True
    else: return False


largest = 0

for n in range(2,10):
    integer = 1
    while True:
        integer+=2
        numString = str(integer)
        for i in range(2,n+1):
            numString += str(integer*i)
        length = len(numString)
        if length<9:
            continue
        elif length>9:
            break
        else:
            if isPandigital(numString):
                largest = max(largest, int(numString))

print largest
            
        
