nota1 = float(input("Digite a 1° nota: "))
nota2 = float(input("Digite a 2° nota: "))
nota3 = float(input("Digite a 3° nota: "))
maiorNota = nota1

if nota3 > maiorNota:
    maiorNota = nota3
if nota2 > maiorNota:
    maiorNota = nota2

if nota1 == nota2 and nota2 == nota3:
    print("=============================================")
    print("Empate total")
elif nota2 == nota3 and (nota2 and nota3) >= maiorNota:
    print("=============================================")
    print("Empate na maior nota")
elif nota2 == nota1 and (nota2 and nota1) >= maiorNota:
    print("=============================================")
    print("Empate na maior nota")
elif nota3 == nota1 and (nota3 and nota1) >= maiorNota:
    print("=============================================")
    print("Empate na maior nota")
 
print("Maior nota é:", maiorNota)