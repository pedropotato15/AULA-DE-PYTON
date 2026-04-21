nota1 = int(input("Digite nota 1: "))
nota2 = int(input('Digite nota 2: '))
faltas = int(input("Digite o numero de faltas: "))

media = (nota1 + nota2) / 2
print("Sua media é igual a", media , ", e você tem", faltas, "faltas")

if media >= 7 and faltas <= 10:
    print("Você está aprovado!")
elif media < 7 and faltas <= 10:
    print("Exame final.")
elif faltas > 10:
    print("Reprovado por faltas")
