from math import sqrt

def findWordValue(word):
    value = 0
    for char in word:
        value+= ord(char) - ord('A')+1
    return value

def isTriangleNumber(number):

    lower = int(sqrt(2*number))
    upper = lower+1

    if lower*upper/2 == number:
        return True
    else:
        return False


filename = 'Problem042.dat'

f=open(filename,'r')
words = f.read()
words = words.replace('\"','')
words = words.split(',')
words.sort()

numOfTriangleWords = 0

for word in words:

    wordValue = findWordValue(word)
    if isTriangleNumber(wordValue):
        numOfTriangleWords +=1

print numOfTriangleWords
