numero1 = float(input("Digite o 1° valor do cálculo: "))
operação = (input("Digite o símbolo da operação do cálculo: "))
numero2 = float(input("Digite o 2° valor do cálculo: "))
resultado = None



if (operação == "+" ) or (operação == "-") or (operação == "*") or (operação == "/"):

    if operação == "/" and numero2 == 0:
        print("Erro: Divisão por zero.")
    else:
        if operação == "+":
            resultado = numero1 + numero2
        elif operação == "-":
            resultado = numero1 - numero2
        elif operação == "*":
            resultado = numero1 * numero2
        elif operação == "/":
            resultado = numero1 / numero2
            
        if resultado % 2 == 0:
            parImpar = "é par,"
        else:
            parImpar = "não é par,"
        if resultado >= 0:
            positivoNegativo = "é positivo,"
        else:
            positivoNegativo = "é negativo,"
        if resultado >= -100 and resultado <= 100:
            intervalo = "e está no intervalo entre 100 e -100,"
        else:
            intervalo = "e não está no intervalo entre 100 e -100,"
   
        print ("O resultado é", resultado, parImpar, positivoNegativo, intervalo)

else:
    print("Operação inválida.")

