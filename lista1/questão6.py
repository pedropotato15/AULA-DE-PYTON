#Pede os anos de nascimento
ano1 = int(input("Digite o ano do 1º irmão: "))
ano2 = int(input("Digite o ano do 2º irmão: "))
ano3 = int(input("Digite o ano do 3º irmão: "))
temporario = 0
#Coloca em ordem crescente do menor para o maior
if ano1 > ano2:
    temporario = ano1
    ano1 = ano2 
    ano2 = temporario
if ano1 > ano3:
    temporario = ano1
    ano1 = ano3
    ano3 = temporario
if ano2 > ano3:
    temporario = ano2
    ano2 = ano3
    ano3 = temporario

#Mostra os anos organizados
print(f"Ordem dos anos: {ano1} anos, {ano2} anos, {ano3} anos.")

# Verifica se são iguais
if ano1 == ano2 and ano2 == ano3:
    print("Trigêmeos")
elif ano1 == ano2 or ano1 == ano3 or ano2 == ano3:
    print("Gêmeos")
else:
    print("Todos diferentes")