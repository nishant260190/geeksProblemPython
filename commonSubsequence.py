'''
Given two strings a and b print whether they contain any common subsequence (non empty) or not.

Input:
The first line contains an integer T denoting number of testcases. Each of the next T lines contains two strings a and b.

Output:
Print 1 if they have a common subsequence (non empty) else 0.

Constraints:
1<=T<=10^5
1<= |a|=|b| <=30
a and b consist of uppercase English letters ('A'....'Z')

Example:
Input:
1
ABEF CADE
Output:
1

Explanation:
AE is a subsequence of both the string so the answer is 1.
'''

noOfTestCases = int(input());
dataArray = [];
for case in range(noOfTestCases):
    arrStr = input();
    dataArray.append(arrStr);

for item in dataArray :
    first, second = item.split();
    firstSet = set(first);
    secondSet = set(second);
    common = firstSet & secondSet
    if len(common) > 0 :
        print(1);


/* another way */

'''
def isCommon(str1, str2):
    for c in str1:
        if c in str2:
            return 1
    return 0

if __name__ == "__main__":
    tc = int(input())
    for _ in range(tc):
        str1, str2 = input().split()
        print( isCommon(str1, str2) )
'''

// one more way

'''
t=int(input().strip())
while t:
    flag=0
    a,b=input().strip().split(' ')
    for i in string.ascii_uppercase[:]:
        if (i in a)&(i in b):
            flag=1
            break
    if flag==1:
        print (1)
    else:
        print (0)
    t-=1
'''
