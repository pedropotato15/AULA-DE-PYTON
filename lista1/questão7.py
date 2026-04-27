#Pede pro usuário três segmentos de reta
segmento1 = int(input("Digite o valor do 1° segmento de reta: "))
segmento2 = int(input("Digite o valor do 2° segmento de reta: "))
segmento3 = int(input("Digite o valor do 3° segmento de reta: "))

#Verifica se os valores podem formar um triângulo e a soma de dois lados deve ser maior que o terceiro
if segmento1 + segmento2 > segmento3 and segmento1 + segmento3 > segmento2 and segmento2 + segmento3 > segmento1:

    #Se todos os lados são iguais é um triângulo equilátero
    if segmento1 == segmento2 and segmento2 == segmento3:
        print("Triângulo equilátero")
    
    #Se apenas dois lados são iguais é um triângulo isósceles
    elif segmento1 == segmento2 or segmento1 == segmento3 or segmento2 == segmento3:
        print("Triângulo isósceles")
    
    #E se todos os lados são diferentes é um triângulo escaleno
    else:
        print("Triângulo escaleno")

# Caso não seguir a regra, não forma um triângulo
else:
    print("Os valores não formam um triângulo.")