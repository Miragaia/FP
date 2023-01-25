def printLocation(p):
    if (p[0] == "a" or p[0] == "h") and (p[1]== "1" or p[1]=="8"):
        print("{} : Corner".format(p))
    elif ((p[0] == "a" or p[0] == "h") and not (p[1]=="1" or p[1]=="8")) or ((p[1]=="1" or p[1]=="8") and not (p[0] == "a" or p[0] == "h")):
        print("{} : Border".format(p))
    else:
        print("{} : Inside".format(p))

def main():
    allpositions =[]
    letters = ("a","b","c","d","e","f","g","h")
    numbers = ("1","2","3","4","5","6","7","8")
    for l in letters:
        for n in numbers:
            allpositions.append(l+n)
    for p in allpositions:
        printLocation(p)
    
    
main()