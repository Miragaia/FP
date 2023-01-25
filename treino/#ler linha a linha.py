#ler linha a linha
for line in file:
    #do something here

#outra maneira
while True:
    line = fin.readline() # returns line to the end
    if line == "": break # empty means end-of-file
    print(repr(line))