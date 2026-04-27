print('Digite "1" para converter pra centímetros, "2" para milímetros ou "3" para quilômetros.')
print("========================================================================================")
distancia = float(input("Digite a distancia em metros: "))
conversao = int(input("Digite para qual unidae voçê que converter: "))

if conversao > 0 and conversao < 4:

    if conversao == 1:
        distancia = distancia * 100
        print("Sua conversão é igual a", distancia,"cm")
    elif conversao == 2:
        distancia = distancia * 1000
        print("Sua conversão é igual a", distancia,"mm")
    elif conversao == 3:
        distancia = distancia / 1000
        print("Sua corversão é igual a", distancia,"km")
    
else:
    print("Opção de conversão inválida.")