print("Categorias de clente: Comum = 1, VIP = 2, Funcionário = 3.")
print("===========================================================")
valorCompra = float(input("Digite o valor da sua compra: "))
categoriaCliente = int(input("Digite a sua categoria de cliente: "))

if categoriaCliente == 1:
    valorFinal = valorCompra
elif categoriaCliente == 2:
    valorFinal = valorCompra - (valorCompra * 0.1)
elif categoriaCliente == 3:
    valorFinal = valorCompra - (valorCompra * 0.2)


print("O valor final de sua compra é:",valorFinal)
