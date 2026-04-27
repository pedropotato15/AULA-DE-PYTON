#Pede para colocar o peso e a altura
peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

#Calcula o IMC pelo peso dividido pela altura ao quadrado
imc = peso / (altura * altura)

#Mostra o valor do IMC
print("============================================")
print("Seu IMC é", imc)

# Classifica o IMC de acordo com a faixa de valor
if imc < 18.5:
    #IMC abaixo de 18.5 é abaixo do peso
    print("Abaixo do peso.")
elif imc < 25:
    #IMC entre 18.5 e 24.9 é considerado normal e mais saudável
    print("Peso normal.")
elif imc < 30:
    #IMC entre 25 e 29.9 coença a ficar mais pesado
    print("Sobrepeso.")
else:
    #IMC a partir de 30 é gordo demais
    print("Obesidade")