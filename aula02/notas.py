CTP = float(input('Qual o valor da CTP? '))
CP = float(input('Qual o valor da CP? '))
NF = int(CTP*0.36 + CP*0.64)
if CTP or CP < 6.5:
    print('NF = código 66')
if 10<= NF >= 20:
    print( 'A nota final é', NF)
else:
    ATPR= float(input('Qual o valor da ATPR? '))
    APR= float(input('Qual o valor da APR? '))
    NF = 0.36*max(CTP, ATPR) + 0.64*max(CP, APR)
    print( ' A nota final é', NF)