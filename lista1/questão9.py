#Solicita dois números e o símbolo da operação
numero1 = float(input("Digite o 1° valor do cálculo: "))
operacao = input("Digite o símbolo da operação do cálculo: ")
numero2 = float(input("Digite o 2° valor do cálculo: "))

#Inicia a variável resultado
resultado = None

#Verifica se a operação digitada é válida
if (operacao == "+") or (operacao == "-") or (operacao == "*") or (operacao == "/"):

    #Trata a operação de divisão por zero
    if operacao == "/" and numero2 == 0:
        print("Erro: Divisão por zero.")
    
    else:
        #Faz a operação de acordo com o símbolo informado
        if operacao == "+":
            resultado = numero1 + numero2
        elif operacao == "-":
            resultado = numero1 - numero2
        elif operacao == "*":
            resultado = numero1 * numero2
        elif operacao == "/":
            resultado = numero1 / numero2
        
        #Verifica se o resultado é par ou não
        if resultado % 2 == 0:
            parImpar = "é par,"
        else:
            parImpar = "não é par,"
        
        #Verifica se o resultado é positivo ou negativo
        if resultado >= 0:
            positivoNegativo = "é positivo,"
        else:
            positivoNegativo = "é negativo,"
        
        #Verifica se o resultado está dentro do intervalo entre -100 e 100
        if -100 <= resultado <= 100:
            intervalo = "e está no intervalo entre -100 e 100,"
        else:
            intervalo = "e não está no intervalo entre -100 e 100,"
   
        #Mostra o resultado com as classificações
        print("O resultado é", resultado, parImpar, positivoNegativo, intervalo)

#Caso a operação for inválida
else:
    print("Operação inválida.")