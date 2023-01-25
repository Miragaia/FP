def posclosest(lst,val):
    i=0
    if len(lst)==0:
        return -1
    for n in lst:
        if i==0 or dif> abs(n-val):
            dif= abs(n-val)
            index=i
        i+=1
    return index+1
            
        



a = posclosest([1,3,7,4,56,76,33,21], 19)
print(a)
    