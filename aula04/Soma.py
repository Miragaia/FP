def leibnizPi4(n):
    for n in range(0, n+1):
     Soma= ((-1)**n)/(2*n+1)
    return(Soma)

a= int(input('Valor? '))
z= leibnizPi4(a)
print('A soma dos',a,'primeiros termos é ',z)
