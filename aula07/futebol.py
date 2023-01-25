lst=[]
def adicionar():
    a = input("Nome da equipa ")
    while a != "":
        lst.append(a)
        a=input("Nome da equipa ")
    return lst

