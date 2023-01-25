x1 = float(input("number? "))
x2 = float(input("number? "))
x3 = float(input('number? '))
if x3<=x1>=x2:
    mx = x1
elif x1<=x2>=x3:
    mx = x2
else:
    mx= x3

print("Maximum:", mx)
