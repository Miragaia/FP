def inputFloatList():
    list = []
    while True:
        a = input('Digite o número ')
        if a == '':
            break
        n = float(a)
        list.append(n)
    return list

def countLower(list, v):
    h = []
    for n in list:
        if n < v:
            h.append(n)
    return h, len(h)

def minmax(list):
    



l = inputFloatList()    
print(countLower(l,5))