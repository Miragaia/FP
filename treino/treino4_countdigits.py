def countdigits(s):
    c=0
    for a in s:
        if a.isdigit():
            c+=1
    return c


print(countdigits('132 ele 4 so 5 pem4nw3'))
print(countdigits('Miguel'))