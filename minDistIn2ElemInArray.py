def minDist(arr, x, y):
    arrLen = len(arr);
    minimunDistance = arrLen + 1;
    for i in range(arrLen) :
        for j in range(i+1, arrLen):
            if ((arr[i]==x and arr[j] == y) or (arr[j]==x and arr[i] == y) ) and (minimunDistance > abs(i-j)):
                minimunDistance = abs(i-j);

    return minimunDistance;
        
  
arr = [1, 5, 3, 7, 2, 8, 3, 4, 5, 9, 9, 3, 1, 3, 2, 9]
print ("Minimum distance between %d and %d is %d\n"%( 4, 7,minDist(arr, 4, 7)));
print ("Minimum distance between %d and %d is %d\n"%( 9, 3,minDist(arr, 9, 3)));
