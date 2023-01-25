from tkinter import filedialog
def main():
    # 1) Pedir nome do ficheiro (experimente cada alternativa):
    #nums = input("File? ")                                  #A
    nums = filedialog.askopenfilename(title="Choose File") #B
    
    # 2) Calcular soma dos números no ficheiro:
    total = fileSum(nums)
    
    # 3) Mostrar a soma:
    print("Sum:", total)


def fileSum(filename):
    total = 0

    with open(nums, "r") as numbers:
        for line in numbers:
            total += float(line)
            
    print(total)
if __name__ == "__main__":
    main()