ts =float(input('segundos? '))
th = ts /3600
thi = int(th)
tm = (th - thi) * 60
tmi = int(tm)
ts = (tm - tmi) *60
tsi = int(ts)
print("{:02d}:{:02d}:{:02d}".format(thi, tmi, tsi))
