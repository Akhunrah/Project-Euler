def XOR(num,key):
    return abs(num-key)

def passToKey(string):

    num = 0
    for char in string:
        num+=ord(char)
    return num

def decrypt(data,key):

    for i in range(len(data)):
        data[i] = XOR(data[i],key)
    return data

def printMessage(data):
    string = ''
    for num in data:
        string+=chr(num)
    print string


    





f=file('Problem059.dat','r')
encryptedData = f.read().split(',')
for i in range(len(encryptedData)):
    encryptedData[i] = int(encryptedData[i])

minKey = abs(255-max(encryptedData))
maxKey = abs(255 - min(encryptedData))

for key in range(minKey,maxKey+1):
    print key
    printMessage(decrypt(encryptedData,key))


##printMessage(decrypt(encryptedData,key))



