noOfTestCases = int(input());
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
