def max2(x1,x2):
    if x1>x2:
        return(x1)
    elif x2>x1:
        return(x2)
    else:
        return(x1)
def max3(x1,x2,x3):
    return(max2(max2(x1, x2),x3))

x1 = float(input('Qual é o valor de x1? '))
x2 = float(input('Qual é o valor de x2? '))
x3 = float(input('Qual é valor de x3? '))
max9= max2(x1,x2)
max10= max3(x1,x2,x3)
print(max10)
