#Pede os anos de nascimento
ano1 = int(input("Digite o ano do 1º irmão: "))
ano2 = int(input("Digite o ano do 2º irmão: "))
ano3 = int(input("Digite o ano do 3º irmão: "))

#Coloca em ordem crescente do menor para o maior
if ano1 > ano2:
    ano1, ano2 = ano2, ano1

if ano1 > ano3:
    ano1, ano3 = ano3, ano1

if ano2 > ano3:
    ano2, ano3 = ano3, ano2

#Mostra os anos organizados
print("Ordem dos anos:", ano1, ano2, ano3)

# Verifica se são iguais
if ano1 == ano2 and ano2 == ano3:
    print("Trigêmeos")
elif ano1 == ano2 or ano1 == ano3 or ano2 == ano3:
    print("Gêmeos")
else:
    print("Todos diferentes")