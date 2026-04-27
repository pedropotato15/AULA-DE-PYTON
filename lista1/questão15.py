
peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))
imc = peso / (altura * altura)
print("============================================")
print("Seu imc é ",imc)

if imc < 18.5:
    print("Abaixo do peso.")
elif imc == 18.5 or imc < 25:
    print("Peso normal.")
elif imc == 25 or imc < 30:
    print("Sobrepeso.")
elif imc >= 30:
    print("Obesidade")
