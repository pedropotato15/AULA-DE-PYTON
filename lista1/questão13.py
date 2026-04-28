#Solicita os atributos do jogador e do monstro
ataque = int(input("Digite o ataque do jogador: "))
defesa = int(input("Digite a defesa do monstro: "))
dado = int(input("Digite o numero do dado que você rolou: "))

#Se tirar 20 no dado dobra o ataque
if dado == 20:
    ataque = ataque * 2
    print("Acerto Crítico")

#Calcula o dano base
dano = (ataque + dado) - defesa

#Se tirar 1 no dado não dá dano
if dado == 1:
    dano = 0
    print("Falha Crítica")

#Garante que o dano não seja negativo
elif dano < 0:
    dano = 0

#Caso seja um ataque normal entre esses números
elif 1 < dado < 20:
    print("Ataque Comum")

#Mostra o dano final que causou
print(f"Você causou {dano} de dano")