with open("aula09\pg3333.txt", "r", encoding="utf-8") as text:
    d = {}
    l = text.read(1)
    while l:
        if l.isalpha():
            l = l.lower()
            d[l] = d.get(l, 0) + 1
        l = text.read(1)

for e in sorted(d, key=lambda e: d[e], reverse=True):
    print(e, d[e])