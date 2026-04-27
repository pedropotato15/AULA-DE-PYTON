#Pede o mês e o dia ao usuário
mes = int(input("Digite um mês: "))
diaMes = int(input("Digite um dia: "))

# Começa assumindo que a data é inválida
dataValida = False

#Verifica fevereiro até 28 dias
if mes == 2 and diaMes > 0 and diaMes <= 28:
    dataValida = True  

#Verifica meses que tem 30 dias
elif mes in [4, 6, 9, 11] and diaMes > 0 and diaMes <= 30:
    dataValida = True  

#Verifica meses que tem 31 dias
elif mes in [1, 3, 5, 7, 8, 10, 12] and diaMes > 0 and diaMes <= 31:
    dataValida = True  

#Se não entrou em nenhuma condição, continua inválida
else:
    dataValida = False

#Mostra o resultado final
if dataValida:
    print("Data válida.")
else:
    print("Data inválida.")