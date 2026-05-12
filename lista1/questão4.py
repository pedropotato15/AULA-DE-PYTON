#Pede a pontuação de três jogadores
jogador1 = float(input("Digite a pontuação do jogador 1: "))
jogador2 = float(input("Digite a pontuação do jogador 2: "))
jogador3 = float(input("Digite a pontuação do jogador 3: "))

#Dá os lugares com os valores informados
lugar1 = jogador1
lugar2 = jogador2
lugar3 = jogador3

#Variável auxiliar para fazer trocas de valores
temporario = 0

#Se o jogador 2 tiver mais pontos que o jogador 1, troca as posições
if lugar2 > lugar1:
    temporario = lugar1
    lugar1 = lugar2
    lugar2 = temporario

#Se o jogador 3 tiver mais pontos que o atual 1º lugar eles trocam
if lugar3 > lugar1:
    temporario = lugar1
    lugar1 = lugar3
    lugar3 = temporario

#Depois de garantir o 1º lugar, verifica a ordem entre 2º e 3º
if lugar3 > lugar2:
    temporario = lugar2
    lugar2 = lugar3
    lugar3 = temporario

#Verifica se tem empate entre todos os jogadores
if lugar1 == lugar2 == lugar3:
    print("empate triplo")

#Verifica o empate entre 1º e 2º lugar
elif lugar1 == lugar2:
    print("1° lugar e 2° lugar empataram")

#Caso for ao contrário mostra o vencedor com maior pontuação
else:
    print(f"1° Lugar venceu com {lugar1} pontos")