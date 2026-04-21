soma = 0

for i in range (3):
    nota = int(input(f"Digite a nota {i}:"))
    soma = soma + nota

media = soma / (i+1)

print("Sua média é igual a, ", media)
