lista_compras = []

while True:
    print("-----LISTA DE COMPRAS-----")
    print("1. Adicionar itens a lista.")
    print("2. Rempver itens da lista.")
    print("3. Visualizar itens da lista.")
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
            print(f"{item} foi removido da lista de compras!")
        else:
            print(f"{item} não encontrado na lista.")
    elif opcao == '3':
        if len (lista_compras) == 0:
            print("A lista de compras está vazia!")
        else:
            for i, item in enumerate (lista_compras):
               print(f"{i+1}.{item}")
    elif opcao == '4':
        print("Saindo da lista...")
        break
    else:
        print("Opção não encontrada, tente novamente.")