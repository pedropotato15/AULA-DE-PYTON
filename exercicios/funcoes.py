
def media_final(lista):
    media = (sum(lista)) / 3
    return media

def analise_num(numero):
    if numero % 2 == 0:
        print("Seu numero é par")
    else:
        print("seu numero é impar")
    if numero > 10:
        print("Seu numero é maior que 10")
    else:
        print("Seu numero é menor que 10")
    if numero <= 6:
        print("Seu numero é igual ou menor que 6")
    else:
        print("Seu numero não é igual ou menor que 6")
    if numero % 1 == 0 and numero % numero == 1:
        print("Seu numero é primo")
    else:
        print("Seu numero não é primo")
    if numero == 2 or numero == 6 or numero == 7 or numero == 8 or numero == 9:
        print("O numero está no conjunto")
    else:
        print("O numero nao está no conjunto")
    return(analise_num)

print(analise_num(0))
    

