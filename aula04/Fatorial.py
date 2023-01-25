def fatorial(n):
    f=1
    while (n>1):
        f=f*n
        n=n-1
    return(f)
 
y = int(input('Qual é o valor de y?'))
z =fatorial(y)
print(y,'!= ',z)