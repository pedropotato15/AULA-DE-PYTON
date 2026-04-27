print("Cadastro Inicial Rede Social do Bem")
print("Tipos de perfil: A = administrador, M = moderador, U = usuario")
print("==============================================================")
perfil = str(input("Digite o seu tipo de perfil: "))

if (perfil == "u" or perfil == "U") or (perfil == "a" or perfil == "A")  or (perfil == "m" or perfil == "M"):
    if (perfil == "a" or perfil == "A"):
        print("Você logou como administrador")
    elif (perfil == "m" or perfil == "M"):
        print("Você logou como moderador")
    elif (perfil == "u" or perfil == "U"):
        print("Você logou como usuário comum")

else:
    print("Perfil ínvalido")
