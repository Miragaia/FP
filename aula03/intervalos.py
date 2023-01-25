a1= float(input('Qual o valor de a1? '))
b1= float(input('Qual o valor de b1? '))
a2= float(input('Qual o valor de a2? '))
b2= float(input('Qual o valor de b2? '))

if a1<= a2 <b1:
    print('True')
elif a1<= b2 <b1:
    print('True')
elif a2<= a1 <b2:
    print('True')
elif a2<= b1 <b2:
    print('True')
else:
    print('False')