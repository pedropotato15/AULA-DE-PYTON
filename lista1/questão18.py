
mes = int(input("Digite um mês: "))
diaMes = int(input("Digite um dia: "))
dataValida = False

if mes == 2 and diaMes <= 28 and diaMes > 0:
    dataValida = True  

elif mes == 4 and diaMes <= 30 and diaMes > 0:
    dataValida = True  
elif mes == 6 and diaMes <= 30 and diaMes > 0:
    dataValida = True  
elif mes == 9 and diaMes <= 30 and diaMes > 0:
    dataValida = True  
elif mes == 11 and diaMes <= 30 and diaMes > 0:
    dataValida = True  

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
else:
    dataValida = False

if dataValida == True:
    print ("Data válida.")
else:
    print ("Data inválida.")