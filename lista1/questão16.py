#Declara o valor das cores do semáforo pro usuário.
print("Cores de semáforo : Vermelho = 1, Amarelo = 2, Verde = 3." )
print("==========================================================")

#Define o valor das variáveis da cor atual do semáforo e da velocidade atual do veículo.
corAtual = int(input("Qual a cor atual do semáforo: "))
velocidadeAtual = int(input("Qual a velocidade atual do veículo (km/h): "))

#Define as condições das multa com if e elif, se nenhuma for verdadeira utiliza o else.
if corAtual == 1 and velocidadeAtual > 0:
    print("Multa gravíssima por avanço.")

elif corAtual == 2 and velocidadeAtual > 60:
    print("Multa por excesso de velocidade no sinal amarelo.")

elif corAtual == 3 and velocidadeAtual > 80:
    print("Multa por excesso de velocidade.")

else:
    print("Condução segura")
