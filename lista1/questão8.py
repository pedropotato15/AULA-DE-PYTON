numeroInt = int(input("Digite um número inteiro: "))

if numeroInt % 2 == 0:
    numeroPar = True
    
else:
    numeroPar = False

if numeroInt % 5 == 0:
    multiploCinco = True
else:
    multiploCinco = False

if numeroPar == True and multiploCinco == True:
    print("O número", numeroInt,"é par e múltiplo de 5")
elif numeroPar == False and multiploCinco == True:
    print("O número", numeroInt,"é ímpar e múltiplo de 5")  
elif numeroPar == True and multiploCinco == False:
    print("O número", numeroInt,"é par e não é múltiplo de 5") 
elif numeroPar == False and multiploCinco == False:
    print("O número", numeroInt,"é ímpar e não é múltiplo de 5")