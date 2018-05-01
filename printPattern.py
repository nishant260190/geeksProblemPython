numberInput = int(input("Enter a number"));
printNumber = 1;
for i in range(1, 2*numberInput):
    if (i == 1 or i == 2*numberInput-1) :
        print(printNumber)
        printNumber += 1;
    else :
        patternRow = str(printNumber) + " " + str(printNumber);
        print(patternRow);
        if i < numberInput :
            printNumber += 1;
        else :
            printNumber -= 1;
