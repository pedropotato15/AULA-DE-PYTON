lista_busca = [9, 8, 7, 12, 0, 13, 21, 2, 7, 0, 7, 1, 12, 32, 12, 33]

# Repetição para popular a lista

opcao = ""
contarEncontrados = 0

while opcao != "69":

    opcao = input("\nDigite a opção desejada: \n   1-Procurar numero.\n   2-Adicionar numeros.\n   3-Deletar numeros.\n   4-Listar numeros.\n   5-Ordenar  \n   6-Contar\n   7-Copiar\n   8-Listar os numeros da copia\n   69-Sair.\n")
    
    # Print para opção de saída do sistema.
    if opcao == "69":
        print("\nPrograma encerrado. Obrigado pela utilização.")

    # Codigo para Adicionar numeros
    if opcao == "1":
        print("\nOpção 1 selecionada.\n")
        print("*" * 30)

        procurado = int(input("Digite um número a pesquisar: "))

        for elementos in lista_busca:
            if elementos == procurado:
                print(f"Analisando o elemento {elementos} ... Valor {procurado} encontrado.")
                contarEncontrados += 1
            else:
                print(f"Analisando o elemento {elementos} ... Valor {procurado} não é o procurado.")

        print(f"Elemento {procurado} encontrado {contarEncontrados} vezes.")

    # Codigo para adicionar numeros
    elif opcao == "2":
        print("Opção 2 selecionada: \n")
        print("*" * 30)

        numeroAdicionar = int(input("Digite um número a adicionar: "))
        lista_busca.append(numeroAdicionar)


    # Codigo para deletar numeros    
    elif opcao == "3":
        print("Opção 3 selecionada: \n")
        print("*" * 30)

        numeroDeletar = int(input("Digite um número a deletar: "))
        lista_busca.remove(numeroDeletar)
    
    # Codigo para listar numeros
    elif opcao == "4":
        print("Opção 4 selecionada: \n")
        print("*" * 30)
        print(lista_busca[0:])

    elif opcao == "5":
        print("Opção 5 selecionada: \n")
        print("*" * 30)
        lista_busca.sort()
        print(lista_busca)
    
    elif opcao == "6":
        print("Opção 6 selecionada: \n")
        print("*" * 30)
        numero = int(input("Digite um numero: "))
        contagem = lista_busca.count(numero)
        print(contagem)
    
    elif opcao == "7":
        print("Opção 7 selecionada: \n")
        print("*" * 30)
        copia_lista_busca = lista_busca.copy()
        print(copia_lista_busca)
    
    elif opcao == "8":
        print("Opção 7 selecionada: \n")
        print("*" * 30)
        print(copia_lista_busca)