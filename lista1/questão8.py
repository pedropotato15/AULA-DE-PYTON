#Pede para o usuário um número inteiro
numeroInt = int(input("Digite um número inteiro: "))

#Verifica se o número é par que é o resto da divisão por 2 igual a 0
if numeroInt % 2 == 0:
    numeroPar = True
else:
    numeroPar = False

#Verifica se o número é múltiplo de 5 se o resto da divisão por 5 igual a 0
if numeroInt % 5 == 0:
    multiploCinco = True
else:
    multiploCinco = False

#Analisa as combinações possíveis se são par ou ímpar e múltiplo de 5 ou não
if numeroPar == True and multiploCinco == True:
    print(f"O número {numeroInt} é par e múltiplo de 5")
elif numeroPar == False and multiploCinco == True:
    print(f"O número {numeroInt} é ímpar e múltiplo de 5")  
elif numeroPar == True and multiploCinco == False:
    print(f"O número {numeroInt} é par e não é múltiplo de 5") 
elif numeroPar == False and multiploCinco == False:
    print(f"O número {numeroInt} é ímpar e não é múltiplo de 5")