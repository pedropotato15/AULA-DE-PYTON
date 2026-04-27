#Mostra as opções de conversão
print('Digite "1" para converter pra centímetros, "2" para milímetros ou "3" para quilômetros.')
print("========================================================================================")

#Pede a distância em metros
distancia = float(input("Digite a distancia em metros: "))

#Pede a opção de conversão
conversao = int(input("Digite para qual unidade você quer converter: "))

#Verifica se a opção digitada está dentro das válidas de 1 a 3
if conversao > 0 and conversao < 4:

    #Converte pra centímetros
    if conversao == 1:
        distancia = distancia * 100
        print("Sua conversão é igual a", distancia, "cm")
    
    # Converte pra milímetros
    elif conversao == 2:
        distancia = distancia * 1000
        print("Sua conversão é igual a", distancia, "mm")
    
    # Converte pra quilômetros
    elif conversao == 3:
        distancia = distancia / 1000
        print("Sua conversão é igual a", distancia, "km")

#Caso a opção for inválida
else:
    print("Opção de conversão inválida.")