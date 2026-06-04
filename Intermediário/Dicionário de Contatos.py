#Agenda de contatos.
agenda = {}
#Aqui estamos criando um dicionário.

def adicionar_contato():
    # O def é usado para definir uma função.
    #"adicionar_contato" é uma função que irá perguntar ao usuário qual contato deseja adicionar e guardará essa informação.
    
    nome = input("Digite o nome: ")
    telefone = input("Digite o telefone: ")
    email = input("Digite o email: ")
    #Aqui estamos pedindo ao usuário que digite o nome, telefone e e-mail.
   
    agenda [nome] = {
        "telefone": telefone,
        "email": email
    }
    #Após o usuário fornecer as informações, elas serão guardadas pela função acima.
    
    print(f"\n{nome} foi adicionado com sucesso!")

def buscar_contato():
    #"buscar_contato" é uma função que irá dar a opção do uruario buscar contatos.
   
    nome = input("Digite o nome do contato que deseja buscar: ")
    #Aqui estamos pedindo ao usuário para fornecer as informações necessárias para buscar o contato.  
   
    if nome in agenda:
        #A função desse if é procurar o nome do contato digitado pelo usuário e imprimir os dados.
        
        contato = agenda[nome]
        print(f"\nNome: {nome}")
        print(f"Telefone: {contato['telefone']}")
        print(f"E-mail: {contato['email']}")
  
    else:

        #Caso não seja identificado pelo if, o else imprimirá a mensagem abaixo. 
        print("\nContato não encontrado na agenda.")

def listar_contatos():
    #"listar_contatos" é a opção que o usuário terá de listar todos os contatos guardados na agenda.
    
    if len(agenda) == 0:
        #O len é usado para verificar se tem alguma coisa guardada na agenda; se não estiver, aparece a mensagem abaixo.
        
        print("\nA agenda está vazia.")
    
    else:
        print("\n====LISTA DE CONTATOS====")
        #A função abaixo é usada para buscar o item digitado pelo usuário e imprimir os dados.
       
        for nome, info in agenda.items():
            
            print(f"\nNome: {nome}")
            print(f"Telefone: {info['telefone']}")
            print(f"E-mail: {info['email']}")
            #Essa expressão de acesso dentro das chaves e dos colchetes serve para acessar as informações guardadas na agenda.

def remover_contato():
#Essa função servirá para remover contatos.
    
    nome = input("Digite o nome do contato que deseja remover: ")
    
    if nome in agenda:
    #O if será usado para verificar se o contato digitado pelo usuário estará na agenda.
       
        del agenda [nome]
        #O del será usado para deletar o nome digitado pelo usuário.
        
        print(f"\n{nome} foi removido da lista.")

    else:

        #Se o usuário não for encontrado pelo if, irá imprimir a mensagem a seguir.
        print(f"{nome} não foi encontrado na agenda.")
        
def menu():
#Essa função mostra o menu e as opções para o usuário escolher.

    while True:
    #O while True é usado como um loop para que o menu seja repetido até o usuário escolher a opção sair.

        print("\n===== AGENDA DE CONTATOS =====")
        print("1. Adicionar contato")
        print("2. Buscar contato")
        print("3. Lista de contatos")
        print("4. Remover contato da agenda")
        print("5. Sair da agenda")
        #Essa é a base do menu.

        opcao = input("Escolha uma opção: ")
        #Aqui o usuário escolherá a opção.
        
        if opcao == '1':
            adicionar_contato()

        elif opcao == '2':
            buscar_contato()

        elif opcao == '3':
            listar_contatos()

        elif opcao == '4':
            remover_contato()

        elif opcao == '5':
            print("\nSaindo...")
            break

        else:
            print("Opção invalida")
        
        #Com o if, elif e else, o menu fica utilizável; assim, o usuário consegue acionar as opções. 
menu()