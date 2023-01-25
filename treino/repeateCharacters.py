def repeatCharacters(s,n):
    c = ''
    if n == 1:
        return s
    elif n == 0:
        return ''
    else:
        for p in s:
            q =  p*n
            c+=q
        return c
  
print(repeatCharacters('gato', 3))