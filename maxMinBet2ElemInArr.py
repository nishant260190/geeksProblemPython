import sys
 
def minDist(arr, x, y):
    arrLen = len(arr);
    minimunDistance = arrLen + 1;
    firstPositionIndex = sys.maxsize;
    firstValueFound = sys.maxsize;
    for i in range(arrLen):
        if (arr[i]==x) or (arr[i]==y):
            if (firstPositionIndex == sys.maxsize) or (arr[i] == firstValueFound):
                firstPositionIndex = i;
                firstValueFound = arr[i];
            else :
                if (arr[i]!=firstValueFound) :
                    minimunDistance = i - firstPositionIndex;
                    break;

    if (minimunDistance == arrLen + 1) :
        print ("Some Values are missing");
        return 0;
    else :
        return minimunDistance;


        
  
arr = [1, 5, 3, 7, 2, 8, 3, 4, 5, 9, 9, 3, 1, 3, 2, 9]
print ("Minimum distance between %d and %d is %d\n"%( 4, 7,minDist(arr, 4, 7)));
print ("Minimum distance between %d and %d is %d\n"%( 9, 3,minDist(arr, 9, 3)));
