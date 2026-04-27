ataque = int(input("Digite o ataque do jogador: "))
defesa = int(input("Digite a defesa do monstro: "))
dado = int(input("Digite o numero do dado que você rolou: "))

if dado == 20:
    ataque = ataque * 2
    print("Acerto Crítico")
    
dano = (ataque + dado) - defesa

if dado == 1:
    dano = 0
    print("Falha Crítica")
elif dano < 0:
    dano = 0
elif dado > 1 and dado < 20:
    print("Ataque Comum")



print("Você causou ", dano," de dano")