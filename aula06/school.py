# Complete o programa!

# a)
def loadFile(school1, lst):
    lst = []
    with open(school1, "r", encoding="utf-8") as values:
        for line in values:
            if line[0].isnumeric():
                value_list = line.split("\t")
                value_list[0] = int(value_list[0])
                lst.append(tuple(value_list))
    return lst
    
# b) Crie a função notaFinal aqui...
def notaFinal(reg):
    nota1 = float(reg[-1])
    nota2 = float(reg[-2])
    nota3 = float(reg[-3])
    return (nota1 + nota2 + nota3) / 3

    

# c) Crie a função printPauta aqui...
def printPauta(lst):
    print("Numero{:^100}Nota".format("Nome"))
    for reg in lst:
        print("{:>6}{:^100}{:4.1f}".format(reg[0], reg[1], notaFinal(reg)))

# d)
def main():
    lst = []
    # ler os ficheiros
    loadFile("school1.csv", lst)
    loadFile("school2.csv", lst)
    loadFile("school3.csv", lst)
    
    # ordenar a lista
    lst.sort()
    
    # mostrar a pauta
    printPauta(lst)


# Call main function
if __name__ == "__main__":
    main()


