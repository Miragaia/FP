def positionDifferenceFirstLastLargest(lst):
    maxn=0
    index=0
    for n in lst:
        if (maxn < n) or (index==0):
            maxn=n
            firstindex=index
        if maxn==n:
            lastindex= index
        index+=1
    diff= lastindex - firstindex
    return diff
                
print(positionDifferenceFirstLastLargest([-1,-22,-3,-4,-5,-6,-22,-1,-7]))