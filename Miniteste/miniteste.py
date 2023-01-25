t=[['coal',45],['rice',50],['iron',5],['rice',42],['coal',45]]
def cargoQuantity(t,m):
    q=0
    for l in t:
        if l[0]==m:
            q+=l[1]
    return q

print(cargoQuantity(t,'rice'))

def unload(t,m,q):
    p = -1
    for c in t[p]:
        if t[p] == '':
            if q == 0:
                return 0
            else:
                return q
        else:
            if c[0]==m:
                q=c[1]-q
    p-=1   
print(unload(t, 'rice', 92))

