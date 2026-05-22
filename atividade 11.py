#Leitor de arquivo de texto.
def ler_arquivo(nome_arquivo): #O def é usado para criar funções.
    try: #Permite testar os códigos em busca de erro.
        with open(nome_arquivo,'r', encoding='UTF-8')as arquivo: #Abre o arquivo em modo leitura e lê usando UTF-8 (lê o texto, evitando problemas com acentos);
            conteudo = arquivo.read() #Guardará todo o conteúdo do arquivo na variável 'conteudo'.
            print("\n====Conteúdo do Arquivo====")
            print(f"{conteudo}")
            #Imprimirá todo o conteúdo do arquivo.
    except FileNotFoundError: #Se o arquivo não for encontrado, imprimir uma mensagem de erro.
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")
    except Exception as e: #O 'Exception as e' servirá para mostrar qualquer erro genérico.
        print(f"Ocorreu um erro ao ler o arquivo: {e}")
nome_do_aquivo = input("Digite o nome do arquivo de texto(.txt): ") #Usado para pedir ao usuário o nome do arquivo.
ler_arquivo(nome_do_aquivo)