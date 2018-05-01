'''Given an array of distinct integers, print all the pairs having positive value and negative value of a number that exists in the array.

NOTE: If there is no such pair in the array , print "0".

Input:
The first line consists of an integer T i.e number of test cases. The first line of each test case consists of an integer n.The next line of each test case consists of n spaced integers.

Output:
Print all the required pairs in the increasing order of their absolute numbers.

Constraints: 
1<=T<=100
1<=n<=1000
-1000<=a[i]<=1000

Example:
Input:
2
6
1 -3 2 3 6 -1
8
4 8 9 -4 1 -1 -8 -9

Output:
-1 1 -3 3 
-1 1 -4 4 -8 8 -9 9 

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
    numbers.sort();
    pairs = '';
    while len(numbers) > 0 :
        if numbers[0] > 0:
            break;
        if numbers[0]*(-1) in numbers :
            pairs = str(numbers[0]) + " " + str(numbers[0]*(-1)) + " " + pairs;
            numbers.remove(numbers[0]*(-1));
            numbers.pop(0);
        else :
            numbers.pop(0);

    if len(pairs) > 0 :
        print(pairs);
    else :
        print("0");
