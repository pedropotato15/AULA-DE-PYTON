#Pede o nome de usuário e a senha
usuario = str(input("Digite seu usuario: "))
senha = int(input("Digite sua senha: "))

#Verifica se usuário e senha estão corretos
if usuario == "admin" and senha == 1234:
    print("Acesso liberado.")

# Mostra usuário incorreto, mas a senha correta
elif usuario != "admin" and senha == 1234:
    print("Usuário não encontrado no sistema.")

#Usuário correto, mas senha incorreta
elif usuario == "admin" and senha != 1234:
    print("Senha incorreta.")

#Usuário e senha incorretos
elif usuario != "admin" and senha != 1234:
    print("Usuario e senha incorretos.")