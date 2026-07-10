
def menu():
    
    print("\n----Menu----")
    print("1 - Adição")
    print("2 - Subtração")
    print("3 - Multiplicaçao")
    print("4 - Divisão")
    print("5 - Saída\n")

    while True:
        operacao = int(input("Digite a sua operação: "))
        if operacao != 5:
            print("\nO programa foi encerrado.\n")
            break
        tabuada = int(input("Digite o numero da tabuada: ") )
        numero = 1
        while numero <= 10:
            if operacao == 1:
                resultado = tabuada + numero
                sinal = "+"
            elif operacao == 2:
                resultado = tabuada - numero
                sinal = "-"
            elif operacao == 3:
                resultado = tabuada * numero
                sinal = "x"
            elif operacao == 4:
                resultado = tabuada / numero
                sinal = ":"
            print(f"{tabuada} {sinal} {numero} = {resultado}")
            numero += 1

entrada = "abcc"
letra_atual = 0

for i in entrada:
    
    print
    letra_atual += 1
    

