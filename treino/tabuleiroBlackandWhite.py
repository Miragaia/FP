
def BlackorWhite():
    s=input('Digite a coordenada ')
    l=s[0]
    n=int(s[1])
    if (l == 'a' or l =='c' or l=='e' or l=='g') and (n%2 != 0):
        print('Black')
    elif(l == 'b' or l =='d' or l=='f' or l=='h') and (n%2 == 0):
        print('Black')
    else:
        print('White')
BlackorWhite()