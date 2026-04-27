saldoAtual = float(input("Digite seu saldo atual: "))
valorSaque = float(input("Digite o valor do seu saque: "))
print("================================================")
saldoNovo = saldoAtual - valorSaque

if valorSaque > 0:
    if saldoNovo > 0:
        print("Saque concluído, seu saldo está positivo")
    elif saldoNovo < 0:
        print("Saque concluído, entrou no cheque especial")
    elif saldoNovo == 0:
        print("Saque concluído, saldo zerado")
else:
    print("Saque inválido")