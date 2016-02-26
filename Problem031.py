comboArray=[]
coins=[1,2,5,10,20,50,100,200]


for target in range(0,201):
    comboArray.append([])
    for coin in coins:
        j=coins.index(coin)
        if j==0:
            comboArray[target].append(1)
        elif coin<=target:
            comboArray[target].append(comboArray[target][j-1]+comboArray[target-coin][j])
        else:
            comboArray[target].append(comboArray[target][j-1])
    print target,comboArray[target]

