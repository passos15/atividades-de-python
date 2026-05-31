#Leitor de arquivo de texto.
from tkinter import Tk #Classe principal do tkinter(é a biblioteca padrão para a criação de Interfaces Gráficas de Usuário), usada para criar janelas gráficas.
from tkinter.filedialog import askopenfilename #Função que abre uma janela para selecionar um arquivo.

def ler_arquivo(): #O def é usado para criar funções.
    
    try: #Permite testar os códigos em busca de erro.

        Tk().withdraw() #tk(Cria uma instância da janela principal). withdraw(Esconde a janela principal (para não aparecer uma janela vazia)).

        nome_arquivo = askopenfilename(title="Selecione um arquivo") #askopenfilename: Abre uma janela para você escolher um arquivo. title: Define o título da janela de seleção.

        if not nome_arquivo: #Se a janela for fechada sem nenhum arquivo selecionado, imprimirá a mensagem a seguir.
            print("Nenhum arquivo selecionado.")
            return

        with open(nome_arquivo,'r', encoding='UTF-8')as arquivo: #Abre o arquivo em modo leitura e lê usando UTF-8 (lê o texto, evitando problemas com acentos).
            conteudo = arquivo.read() #Guardará todo o conteúdo do arquivo na variável 'conteudo'.
            print("\n====Conteúdo do Arquivo====")
            print(f"{conteudo}")
            #Imprimirá todo o conteúdo do arquivo.
    
    except FileNotFoundError: #Se o arquivo não for encontrado, imprimir uma mensagem de erro.
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")
    
    except Exception as e: #O 'Exception as e' servirá para mostrar qualquer erro genérico.
        print(f"Ocorreu um erro ao ler o arquivo: {e}")

ler_arquivo()