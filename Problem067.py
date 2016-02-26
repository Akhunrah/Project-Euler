import numpy

f=open('Problem067.dat','r')

lines = f.readlines()

numOfCols = len(lines)
numOfRows = len(lines[numOfCols-1].split())

matrix = numpy.zeros((numOfRows,numOfCols))

for i in range(numOfRows):
    for j in range(i+1):
        row = lines[i].split()
        matrix[i][j] = int(row[j])

for i in range(numOfRows-2,-1,-1):
    for j in range(i+1):
        matrix[i,j] = matrix[i,j]+max(matrix[i+1,j],matrix[i+1,j+1])

print matrix[0,0]
