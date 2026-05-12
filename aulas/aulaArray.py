# primeira questao
x = 1
while x <= 100:
    print (x)
    x = x + 1

#segunda questãp
y = 1
while y > 50 and y < 100:
    print (x)
    x = x + 1

#terceira questão:
z = 10
while z >= 0 and z <= 10:
    print (z)
    z = z - 1
print("fogo!")

#quarta questao
final = int(input("Digite o ultimo número da contagem: "))
x = 1
while x <= final:
    if x % 2 != 0:
        print(x)
    x = x + 1

#quinta questão
inicio = int(input("Tabuada inicia em: "))
fim = int(input("Tabuada termina em"))
num = int(input("Tabuada de: "))
x = 1
print("==============================================")

while x <= 10:
    resultado = (x * num)
    print(f"{num} x {x} = {resultado}")
    x = x + 1

#sexta questão