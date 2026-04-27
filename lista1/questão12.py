#Pede pro usuário um ano
ano = int(input("Digite um ano: "))

#Verifica se o ano tá dentro de um intervalo
if 1000 <= ano <= 9999:

   #Ano bissexto divide por 4, tirando os divisíveis por 100 só se também sejam por 400
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        print(ano, "é um ano bissexto")
    else:
        print(ano, "é um ano comum")

#Caso o ano esteja fora do intervalo
else:
    print("Número incorreto")