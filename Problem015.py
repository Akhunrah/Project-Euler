# Basically just use Pascal's triangle.

import numpy

numOfRows = 20
numOfCols = 20

matrix = numpy.zeros((numOfRows,numOfCols))


for i in range(numOfRows):
    for j in range(numOfCols):
        if i==0 and j==0:
            matrix[i][j]=2
        elif i==0:
            matrix[i][j]=1+matrix[i][j-1]
        elif j==0:
            matrix[i][j]=1+matrix[i-1][j]
        else:
            matrix[i][j]=matrix[i-1][j]+matrix[i][j-1]

print matrix[numOfRows-1][numOfCols-1]
    
