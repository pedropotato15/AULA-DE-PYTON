usuario = str(input("Digite seu usuario: "))
senha =  int(input("Digite sua senha: "))

if usuario == "admin" and senha == 1234:
    print("Acesso liberado.")
elif usuario != "admin" and senha == 1234:
    print("Usuário não encontrado no sistema.")
elif usuario == "admin" and senha != 1234:
    print("Senha incorreta.")
elif usuario != "admin" and senha != 1234:
    print("Usuario e senha incorretos.")