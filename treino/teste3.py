'''def position(lst):
    mx=''
    mn=''
    for n in lst:
        mx=lst[0]
        mn=lst[0]
        cmx=0
        cmn=0
        if n > mx:
            mx=n
            cmx=0
        elif n < mn:
            mn=n
            cmn=0
        else:
            cmx+=1
            cmn+=1
    dist=cmx-cmn
    return dist

print(position([4,7,8,4,2,0]))'''
