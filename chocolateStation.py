'''noOfTestCases = int(input());
chocolateArray = [];
cltCostArray = [];
for case in range(noOfTestCases):
    noOfStations = int(input());
    arrStr = input();
    chocolateArray.append(arrStr);
    cost = int(input());
    cltCostArray.append(cost);


testCaseIndex = 0;
while testCaseIndex < noOfTestCases :
    chocStr = chocolateArray[testCaseIndex].split();
    finalChocArr = [int(x) for x in chocStr];
    chocBuy = 1;
    noOfChocsHave = 1;
    prevStationChocCount = finalChocArr[0];
    for i in range(1, len(finalChocArr)) :
        print("***************");
        chocRecvd = prevStationChocCount - finalChocArr[i];
        noOfChocsHave = noOfChocsHave + chocRecvd;
        prevStationChocCount = finalChocArr[i];
        print("no of chocs hv");
        print(noOfChocsHave);
        if noOfChocsHave < 0 :
            chocBuy = chocBuy + noOfChocsHave;
            noOfChocsHave = 0;
        print("chocs buy");
        print(chocBuy);
    print(chocBuy*cltCostArray[testCaseIndex]);
    testCaseIndex +=1;
'''

testCases = int(input())
for test in range(testCases):
    stations = int(input())
    myList = input().split()
    price = int(input())
    buy = int(myList[0])
    chocolates = 0
    index = 0
    while(index < (stations-1)):
        move = int(myList[index]) - int(myList[index+1])
        chocolates += move
        if(chocolates < 0):
            buy += abs(chocolates)
            chocolates = 0 
        index += 1
    print (buy*price)
