#Pede pra colocar três notas no formato decimal
nota1 = float(input("Digite a 1° nota: "))
nota2 = float(input("Digite a 2° nota: "))
nota3 = float(input("Digite a 3° nota: "))

#Indica que a variável maiorNota é nota1 igual a maior nota
maiorNota = nota1

#Verifica se a terceira nota é maior
if nota3 > maiorNota:
    maiorNota = nota3  # Atualiza a maiorNota

#Verifica se a segunda nota é maior
if nota2 > maiorNota:
    maiorNota = nota2  # Atualiza a maiorNota

#Verifica se todas as notas são iguais
if nota1 == nota2 and nota2 == nota3:
    print("=============================================")
    print("Empate total")

#Verifica se a nota2 e nota3 são iguais na maiorNota
elif nota2 == nota3 and (nota2 and nota3) >= maiorNota:
    print("=============================================")
    print("Empate na maior nota")

#Verifica se tem empate entre nota2 e nota1 na maiorNota
elif nota2 == nota1 and (nota2 and nota1) >= maiorNota:
    print("=============================================")
    print("Empate na maior nota")

#Verifica se tem empate entre nota3 e nota1 na maiorNota
elif nota3 == nota1 and (nota3 and nota1) >= maiorNota:
    print("=============================================")
    print("Empate na maior nota")

#Mostra a maior nota encontrada
print(f"Maior nota é: {maiorNota}")