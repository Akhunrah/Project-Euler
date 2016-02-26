def nameValue(name):
    value = 0
    for char in name:
        value+= ord(char) - ord('A')+1
    return value

f = open('Problem022.dat','r')

names = f.read()
names = names.replace('\"','')
names = names.split(',')
names.sort()

scoreSum = 0
for name in names:
    scoreSum += nameValue(name)*(names.index(name)+1)
    print names.index(name)+1,nameValue(name),scoreSum


