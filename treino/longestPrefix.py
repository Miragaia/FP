s= input('String:')
def longestPrefixrepeated(s):
    p = s[:len(s)//2]
    while len(p)>0:
        if p in s[len(p):]:
            return p
        else:
            p=p[:len(p)-1]
        return p
