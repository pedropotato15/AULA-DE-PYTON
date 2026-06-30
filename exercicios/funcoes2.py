from funcoes import media_final


qnt_notas = int(input("Quantidade de notas: "))
lista_notas = []

for i in range(qnt_notas):
    valor = int(input("Digite a nota: "))
    lista_notas.append(valor)

print(media_final(lista_notas))



