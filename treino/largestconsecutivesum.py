def largestConsecutiveSum(arr):
    maiorsoma = 0
    for i in range(len(arr)-1):
        if (i == 0) or (maiorsoma < arr[i] + arr[i+1]):
            maiorsoma = arr[i] + arr[i+1]
    return maiorsoma

print(largestConsecutiveSum([1,2,7,4,5,8,2,3,1,2,5,5,6,2,1,2,3,4,7]))