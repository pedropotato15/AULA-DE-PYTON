ano = int(input("Digite um ano: "))
anoBissexto = False
anoValido = False

if ano <= 9999 and ano >= 1000:
    anoValido = True 

    if anoValido == True and (ano % 100 == 0):
        if anoValido == True and (ano % 400 == 0):
            print(ano, "é um ano bissexto")
        else:
            print(ano, "é um ano comum")

    elif anoValido == True and (ano % 4 == 0):
            print(ano, "é um ano bissexto")
    else:
        print(ano, "é um ano comum")
else:
    print("Número incorreto")
