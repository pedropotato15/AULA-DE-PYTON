segmento1 = int(input("Digite o valor do 1° segmento de reta: "))
segmento2 = int(input("Digite o valor do 2° segmento de reta: "))
segmento3 = int(input("Digite o valor do 3° segmento de reta: "))

if segmento1 + segmento2 > segmento3 and segmento1 + segmento3 > segmento2 and segmento2 + segmento3 > segmento1:

    if segmento1 == segmento2 and segmento2 == segmento3:
        print("Triângulo equilátero")
    elif segmento1 == segmento2 or segmento1 == segmento3 or segmento2 == segmento3:
        print("Triângulo isósceles")
    else:
        print("Triângulo escaleno")

else:
    print("Os valores não formam um triângulo.")