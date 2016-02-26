from common_functions import fibonacci

def countDigits(number):
    return len(str(number))

num0=1
num1=1
i=3
while True:
    number=num0+num1
    
    if countDigits(number)>=1000:
        print i,number
        break

    num0=num1
    num1=number
    
    i+=1
