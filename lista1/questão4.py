jogador1 = float(input("Digite a pontuação do jogador 1: "))
jogador2 = float(input("Digite a pontuação do jogador 2: "))
jogador3 = float(input("Digite a pontuação do jogador 3: "))
lugar1 = jogador1
lugar2 = jogador2
lugar3 = jogador3
temporario = 0

if lugar2 > lugar1:
    temporario = lugar1
    lugar1 = lugar2
    lugar2 = temporario

if lugar3 > lugar1:
    temporario = lugar1
    lugar1 = lugar3
    lugar3 = temporario

if lugar3 > lugar2:
    temporario = lugar2
    lugar2 = lugar3
    lugar3 = temporario

if lugar1 == lugar2 == lugar3:
    print("empate triplo")
elif lugar1 == lugar2:
    print ("1° lugar e 2° lugar empataram") 
else:
    print("1° Lugar venceu com", lugar1,"pontos")

