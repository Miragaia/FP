CTP = float(input('Introduza o valor obtido na sua CTP: '))
CP = float(input('Introduza o valor obtido na sua CP: '))

if ((CTP*0.33+CP*0.64)-int((CTP*0.33+CP*0.64))) >= 0.5:
    x =1
else:
    x=0

nf= int(CTP*0.33+CP*0.64) + x

if (CTP or CP) < 6.5:
    print('Code 66')
elif nf < 10 or nf>20:
    ATPR = float(input('Introduza o valor obtido na sua ATPR: '))
    APR = float(input('Introduza o valor obtido na sua APR: '))
    if ((ATPR*0.33+APR*0.64)-int((ATPR*0.33+APR*0.64))) >= 0.5:
        y =1
    else:
        y=0 
    nf2 = int(ATPR*0.33+APR*0.64) + y
    if (ATPR or APR) < 6.5:
        print('Code 66')
    else:
        print(nf2)
else:
    print(nf)
    

