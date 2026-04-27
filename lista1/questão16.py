#Mostra as opções de cores do semáforo
print("Cores de semáforo : Vermelho = 1, Amarelo = 2, Verde = 3." )
print("==========================================================")

# Pede os dados ao usuário
corAtual = int(input("Qual a cor atual do semáforo: "))
velocidadeAtual = int(input("Qual a velocidade atual do veículo (km/h): "))

#Verifica possíveis infrações
if corAtual == 1 and velocidadeAtual > 0:
    # Andou no vermelho
    print("Multa gravíssima por avanço.")

elif corAtual == 2 and velocidadeAtual > 60:
    #Muito rápido no amarelo
    print("Multa por excesso de velocidade no sinal amarelo.")

elif corAtual == 3 and velocidadeAtual > 80:
    #Acima do limite no verde
    print("Multa por excesso de velocidade.")

else:
    #Situação normal
    print("Condução segura")