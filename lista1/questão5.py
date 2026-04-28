#Pede para o usuário o valor de três produtos
produto1 = float(input("Digite o valor do 1° produto: "))
produto2 = float(input("Digite o valor do 2° produto: "))
produto3 = float(input("Digite o valor do 3° produto: "))

#Inicia as variáveis mostrando que o produto1 é mais caro e o mais barato
produtoCaro = produto1
produtoBarato = produto1

#Verifica qual é o produto mais caro
if produto3 > produtoCaro:
    produtoCaro = produto3  #Atualiza o mais caro

if produto2 > produtoCaro:
    produtoCaro = produto2  #Atualiza o mais caro

#Verifica qual é o produto mais barato
if produto3 < produtoBarato:
    produtoBarato = produto3  #Atualiza o mais barato

if produto2 < produtoBarato:
    produtoBarato = produto2  #Atualiza o mais barato

#Calcula a diferença entre o produto mais caro e o barato
diferencaProduto = (produtoCaro - produtoBarato)

#Mostra os resultados depois do print separador
print("=============================================================")
print(f"Produto mais caro custa: R${produtoCaro:.2f}")
print(f"Produto mais barato custa: R${produtoBarato:.2f}")
print(f"Diferença entre os produtos é de R${diferencaProduto:.2f}")