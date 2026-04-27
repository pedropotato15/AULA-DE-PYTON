#Diz para o usuário o saldo atual e o valor que precisa sacar
saldoAtual = float(input("Digite seu saldo atual: "))
valorSaque = float(input("Digite o valor do seu saque: "))

#Mostra uma linha que separa na tela
print("================================================")

#Calcula o novo saldo depois do saque
saldoNovo = saldoAtual - valorSaque

#Verifica se o valor do saque é válido
if valorSaque > 0:
    
    #Verifica se depois do saque o saldo continua positivo
    if saldoNovo > 0:
        print("Saque concluído, seu saldo está positivo")
    
    #Verifica se o saldo ficou negativo para usar o cheque especial
    elif saldoNovo < 0:
        print("Saque concluído, entrou no cheque especial")
    
    #Verifica se o saldo ficou zerado
    elif saldoNovo == 0:
        print("Saque concluído, saldo zerado")

#Caso o valor do saque seja inválido por estar zerado ou negativo
else:
    print("Saque inválido")