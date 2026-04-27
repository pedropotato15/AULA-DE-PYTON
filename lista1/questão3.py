#Mostra o título do sistema
print("Cadastro Inicial Rede Social do Bem")

#Mostra os tipos de perfil disponíveis
print("Tipos de perfil: A = administrador, M = moderador, U = usuario")

#Linha que separa para organização visual
print("==============================================================")

#Solicita ao usuário o tipo de perfil e armazena como string
perfil = str(input("Digite o seu tipo de perfil: "))

#Verifica se o que foi digitado bate com algum perfil válido
if (perfil == "u" or perfil == "U") or (perfil == "a" or perfil == "A") or (perfil == "m" or perfil == "M"):
    
    #Verifica se é administrador
    if (perfil == "a" or perfil == "A"):
        print("Você logou como administrador")
    
    #Verifica se é moderador
    elif (perfil == "m" or perfil == "M"):
        print("Você logou como moderador")
    
    #Verifica se é usuário comum
    elif (perfil == "u" or perfil == "U"):
        print("Você logou como usuário comum")

#Caso o valor que foi digitado não coincidir com algum perfil válido 
else:
    print("Perfil ínvalido")