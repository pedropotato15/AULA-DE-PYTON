#Mostra as opções
print("Privacidade: 1 = Público, 2 = Amigos, 3 = Privado")
print("Visitante: 1 = Estranho, 2 = Amigo, 3 = Dono")

#Pede os dados
privacidade = int(input("Digite o nível da postagem: "))
visitante = int(input("Digite o tipo de visitante: "))

#Verifica o acesso
if privacidade == 1:
    # Público: qualquer um pode acessar
    print("Acesso Permitido")

elif privacidade == 2:
    #Amigos: apenas amigo ou dono
    if visitante == 2 or visitante == 3:
        print("Acesso Permitido")
    else:
        print("Acesso Negado")

elif privacidade == 3:
    #Privado: só o dono
    if visitante == 3:
        print("Acesso Permitido")
    else:
        print("Acesso Negado")

else:
    #Caso for inválido
    print("Opção inválida")