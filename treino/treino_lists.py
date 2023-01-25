def inputfloatlist():
    print('Digite um valor para adicinar à lista, para terminar nao introduza nenhum valor')
    lst=[]
    while True:
        a = input('Digite um número ')
        if a == '':
            break
        n = int(a)
        lst.append(n)
    
def countLower(lst, v):
    c = 0
    for p in lst:
        if p < v:
            c+= 1
    print(c)

def minmax(lst):
	if lst == []:
		return "none"
	minin = lst[0]
	maxi = lst[0]
	for n in lst:
		if n > maxi:
			maxi = n
		if n < minin:
			minin = n
	return minin, maxi
        


lst=[1,5,6,7,9,12,34,56,87,3,2,4]
v=float(input('Qual o valor de v? '))
