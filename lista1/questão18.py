# Pede o mês e o dia ao usuário
mes = int(input("Digite um mês: "))
diaMes = int(input("Digite um dia: "))

# Começa assumindo que a data é inválida
dataValida = False

# Verifica fevereiro até 28 dias
if mes == 2 and diaMes <= 28 and diaMes > 0:
    dataValida = True  

# Verifica meses que tem 30 dias
elif mes == 4 and diaMes <= 30 and diaMes > 0:
    dataValida = True  
elif mes == 6 and diaMes <= 30 and diaMes > 0:
    dataValida = True  
elif mes == 9 and diaMes <= 30 and diaMes > 0:
    dataValida = True  
elif mes == 11 and diaMes <= 30 and diaMes > 0:
    dataValida = True  

# Verifica meses que tem 31 dias
elif mes == 1 and diaMes <= 31 and diaMes > 0:
    dataValida = True  
elif mes == 3 and diaMes <= 31 and diaMes > 0:
    dataValida = True  
elif mes == 5 and diaMes <= 31 and diaMes > 0:
    dataValida = True  
elif mes == 7 and diaMes <= 31 and diaMes > 0:
    dataValida = True  
elif mes == 8 and diaMes <= 31 and diaMes > 0:
    dataValida = True  
elif mes == 10 and diaMes <= 31 and diaMes > 0:
    dataValida = True  
elif mes == 12 and diaMes <= 31 and diaMes > 0:
    dataValida = True  

# Se não entrou em nenhuma condição, continua inválida
else:
    dataValida = False

# Mostra o resultado final
if dataValida == True:
    print ("Data válida.")
else:
    print ("Data inválida.")