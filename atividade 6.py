    #Lista de compras.
lista = [] #Os colchetes indicam que os valores dentro deles pertencem a uma lista.

while True:  #while True cria um loop infinito, ou seja, o código continuará se repetindo até encontrar um break, que encerra o loop.
    print("===LISTA DE COMPRAS===")
    print("1. Adicionar item.")
    print("2. Remover item.")
    print("3. Visualizar lista.")
    print("4. Sair")
    opcao = input("Digite uma opção: ")
    #No menu o usuario pode escolher uma das opções do menu e o valor digitado é armazenado na variável "opcao".

    if opcao == '1': #Se o usuario digitar a opção 1, esse bloco será acionado. 
        item = input("Digite o item que deseja adicionar: ")
        lista.append(item) #Adicionará o item digitado pelo usuário em 'append' e guardará.
        print(f"{item} foi adicionado a lista!")

    elif opcao == '2': #Se o usuario digitar a opção 2, esse bloco será acionado.
        item = input("Digie o item que deseja remover: ")
        if item in lista: #buscará o item na lista.
            lista.remove(item) #Caso o item estejá na lista será rremovido.
            print(f"{item} foi removido da lista!")
        else: #Caso o item não seja localizado imprimirar a mensagem abaixo.
            print(f"{item} não foi encontrado na lista.")
    
    elif opcao == '3': #Se o usuario digitar a opção 3, esse bloco será acionado.
        if lista:
            print("\n---SUA LISTA---")
            for i, item in enumerate(lista): #Enumera todos os itens da lista a partir de 1 (i = posição).
                print(f"{i+1}.{item}")
        else: #Caso a lista está vazia imprimira essa mensagem.
            print("Sua lista está vazia.")
    
    elif opcao == '4': #Se o usuario digitar a opção 4, esse bloco será acionado.
        print("Saindo...")
        break #Encera completamente o loop e fecha o programa.
    
    else: #Caso não seja nenhuma das opções essa será a mensagem imprimida.
        print("Opção não encontrada, tente novamente...")