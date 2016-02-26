import numpy
from common_functions import findLargerNumber

f=open('Problem011.dat','r')

lines = f.readlines()

numOfRows = len(lines[0].split())
numOfCols = len(lines)

matrix = numpy.zeros((numOfRows,numOfCols))

for i in range(numOfRows):
    row = lines[i].split()
    for j in range(numOfCols):
        entry = int(row[j])
        matrix[i][j]=entry

largest = 0
product = 0

#Sum down
for j in range(numOfCols):
    product = 0
    for i in range(numOfRows-4):
        product = matrix[i][j]*matrix[i+1][j]*matrix[i+2][j]*matrix[i+3][j]
        largest = findLargerNumber(product,largest)

#Sum right
for i in range(numOfRows):
    product=0
    for j in range(numOfCols-4):
        product = matrix[i][j]*matrix[i][j+1]*matrix[i][j+2]*matrix[i][j+3]
        largest = findLargerNumber(product,largest)

#Sum diagonally down
for i in range(numOfRows-4):
    product=0
    for j in range(numOfCols-4):
        product = matrix[i][j]*matrix[i+1][j+1]*matrix[i+2][j+2]*matrix[i+3][j+3]
        largest = findLargerNumber(product,largest)

#Sum diagonally up
for i in range(3,numOfRows):
    product=0
    for j in range(numOfCols-4):
        product = matrix[i][j]*matrix[i-1][j+1]*matrix[i-2][j+2]*matrix[i-3][j+3]
        largest = findLargerNumber(product,largest)

print largest



