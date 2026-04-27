produto1 = float(input("Digite o valor do 1° produto: "))
produto2 = float(input("Digite o valor do 2° produto: "))
produto3 = float(input("Digite o valor do 3° produto: "))
produtoCaro = produto1
produtoBarato = produto1


if produto3 > produtoCaro:
    produtoCaro = produto3
if produto2 > produtoCaro:
    produtoCaro = produto2

if produto3 < produtoBarato:
    produtoBarato = produto3
if produto2 < produtoBarato:
    produtoBarato = produto2

diferençaProduto = (produtoCaro - produtoBarato)

print("=============================================================")
print("Produto mais caro custa:",produtoCaro,"R$")
print("Produto mais barato custa:",produtoBarato,"R$")
print("Diferença entre os produtos é de",diferençaProduto,"R$")    