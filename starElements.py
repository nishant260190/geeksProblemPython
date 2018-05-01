'''
Given an unsorted array. The task is to find all the star and super star elements in the array. Star are those elements which are strictly greater than all the elements on its right side. Super star are those elements which are strictly greater than all the elements on its left and right side.

Note: Assume first element (A[0]) is greater than all the elements on its left side, And last element (A[n-1]) is greater than all the elements on its right side.

Input:
The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. Each test case consists of two lines. First line of each test case contains an Integer N denoting size of array and the second line contains N space separated elements.

Output:
For each test case, print the space separated star elements and then in new line print super star elements. If no super star element present in array then print "-1".

Constraints:
1<=T<=200
1<=N<=106
1<=A[i]<=106

Example:
Input:
2
6
4 2 5 7 2 1
3
8 6 5

Output:
7 2 1
7
8 6 5
8
'''
noOfTestCases = int(input());
dataArray = [];
for case in range(noOfTestCases):
    noOfElem = input();
    arrStr = input();
    dataArray.append(arrStr);

for item in dataArray :
    intArr = item.split();
    numbers = [ int(x) for x in intArr ];
    i = 1;
    starElements = [];
    maxNumber = numbers[0];
    for elem in range(0, len(numbers)-1):
        isStar = True;
        if numbers[elem] > maxNumber :
            maxNumber = numbers[elem];
        for nextElem in range(i, len(numbers)):
            if numbers[elem] > numbers[nextElem] :
                pass;
            else :
                isStar = False;
                break;
        i = i + 1;
        if isStar == True :
            starElements.append(numbers[elem]);
    starElements.append(numbers[-1]);
    print(starElements);
    print(maxNumber);

    ''' best way to iterate reverse array and keep track of max elem'''
