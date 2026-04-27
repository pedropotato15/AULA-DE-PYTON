#Mostra quais são as categorias disponíveis
print("Categorias de cliente: Comum = 1, VIP = 2, Funcionário = 3.")
print("===========================================================")

#Solicita o valor da compra e a categoria do cliente
valorCompra = float(input("Digite o valor da sua compra: "))
categoriaCliente = int(input("Digite a sua categoria de cliente: "))

#Inicia o valor final com o valor original se não tiver desconto
valorFinal = valorCompra

#Aplica o desconto dependendo a categoria
if categoriaCliente == 1:
    #Cliente comum não tem desconto
    valorFinal = valorCompra

elif categoriaCliente == 2:
    #Cliente VIP tem 10% de desconto
    valorFinal = valorCompra - (valorCompra * 0.1)

elif categoriaCliente == 3:
    #Funcionário tem 20% de desconto
    valorFinal = valorCompra - (valorCompra * 0.2)

else:
    #Mostra se a categoria for inválida
    print("Categoria inválida.")

#Mostra o valor final da compra
print("O valor final de sua compra é:", valorFinal)