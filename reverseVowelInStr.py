inpstr = input("Enter the string");
strList = list(inpstr);

vowels = ['a', 'e', 'i', 'o', 'u'];
startIndex = 0;
lastIndex = len(strList) - 1;

while(startIndex < lastIndex) :
    if (strList[startIndex] not in vowels) :
        startIndex = startIndex + 1;
        continue;
    if (strList[lastIndex] not in vowels):
        lastIndex = lastIndex - 1;
        continue;

    curentLetter = '';
    curentLetter = strList[startIndex];
    strList[startIndex] = strList[lastIndex];
    strList[lastIndex] = curentLetter;

    startIndex = startIndex + 1;
    lastIndex = lastIndex - 1;

print(''.join(strList));
