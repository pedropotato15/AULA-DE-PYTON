salarioBruto = float(input("Digite seu salário: "))

taxa = 0
if salarioBruto <= 2000:
    taxa = 0
elif salarioBruto <= 4000:
    taxa = 10
elif salarioBruto >= 6000:
    taxa = 20


imposto = salarioBruto * (taxa / 100)
salarioLiquido = salarioBruto - imposto

print(imposto)
print(salarioLiquido)


