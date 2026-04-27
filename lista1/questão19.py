# Solicita as notas e o número de faltas
nota1 = int(input("Digite nota 1: "))
nota2 = int(input("Digite nota 2: "))
faltas = int(input("Digite o numero de faltas: "))

#Calcula a média das duas notas
media = (nota1 + nota2) / 2

#Mostra a média e as faltas
print("Sua media é igual a", media, ", e você tem", faltas, "faltas")

#Verifica a situação do aluno
if media >= 7 and faltas <= 10:
    #Aprovado por média e frequência
    print("Você está aprovado!")

elif media < 7 and faltas <= 10:
    #Não atingiu a média, mas pode fazer exame
    print("Exame final.")

elif faltas > 10:
    #Reprovado por muitas faltas
    print("Reprovado por faltas")
