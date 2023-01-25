l = float(input('Quantos litros vai introduzir? '))
if l<=40 :
    p = 1.4*l
    print('O valor a pagar é ',p, 'euros')
else:
    p =1.26*l
    print('O valor a pagar é ',p, 'euros')