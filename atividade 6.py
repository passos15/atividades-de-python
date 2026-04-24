lista_compras = []

while True:
    print("\n----- Lista de compras -----\n")
    print("1. Adicionar item a lista")
    print("2. Remover item da lista")
    print("3. Vizualizar lista")
    print("4. Sair")
    opcao = input("Digite a opção desejada: ")
    
    if opcao == '1':
        item = input("Digite o item que deseja adicionar: ")
        lista_compras.append(item)
        print(f"{item} foi adicionado a lista!")
    elif opcao == '2':
        item = input("Digite o item que deseja remover: ")
        if item in lista_compras:
            lista_compras.remove(item)
            print(f"{item} removido da lista!")
        else:
            print("Item não encontrado na lista.")
    elif opcao  == '3':
        if len (lista_compras) == 0:
            print(" A lista está vazia.")
        else:
            for indice, item in enumerate (lista_compras, start = 1):
                print(f"{indice}.{item}")
    elif opcao == '4':
        print("Saindo do programa!")
        break
    else:
        print("opção não encontrada, tente novamente.")