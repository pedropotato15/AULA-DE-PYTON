#Pede o salário bruto do usuário
salarioBruto = float(input("Digite seu salário: "))

#Inicia a taxa de imposto
taxa = 0

# Define a taxa de acordo com a faixa salarial
if salarioBruto <= 2000:
    taxa = 0  # Isento

elif salarioBruto <= 4000:
    taxa = 10  #10% de imposto

elif salarioBruto <= 6000:
    taxa = 15  #15% de imposto

else:
    taxa = 20  #20% de imposto

#Calcula o valor do imposto
imposto = salarioBruto * (taxa / 100)

# Calcula o salário líquido depois do desconto
salarioLiquido = salarioBruto - imposto

#Mostra os resultados
print(f"Imposto: {imposto:.2f}")
print(f"Salário líquido: {salarioLiquido:.2f}")


