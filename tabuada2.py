# Tabuada!

print("\n\t\t\t -- Tabuada  -- \n")

while True:
    print("\n\t\t\t 1.Tabuada \n")
    print("\n\t\t\t 2. Sair \n")
    op = int(input("\nOpção: "))

    if op == 1:
        #Endrada
        nume = int(input("\n Qual número? \n"))
        repet = int(input("\n Quantas vezes? \n"))

        #Saida
        while repet >= 0:
            total = nume * repet
            print("\n\t\t {} * {} = {} \n".format(nume,repet,total))
            repet = repet - 1
    
    elif op == 2:
        print("\n\nFinal da execução\n\n")
        break
    else:
        if op >= 3:
            print("\n\nOpção {} incorreta.\n\n".format(op))