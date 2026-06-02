import pandas as pd #Pandas  é a biblioteca principal para trabalhar dados em planilhas no python (PD é uma abreviação para facilitar).

try:
     
        df = pd.read_csv('dados_clientes.csv') #df é uma variavel que irá armazenar a tabela. // pd.read_csv ler o arquivo e armazena os dados.
        
        print("\n===Análisa de Dados de Clientes===")
        print("DataFrame Original:") #É uma estrutura de dados semelhante a uma planilha.
        print(df)
        #Exibe a tabela completa.

        #Media de idade e renda dos clientes.
        
        media_idade = df['Idade'].mean() #df['Idade'] seleciona a coluna Idade. // .mean() calcula a media da coluna selecionada. 
        media_renda = df['Renda'].mean() 
        print(f"\nMédia de Idade: {media_idade:.2f} anos")
        print(f"Média de Renda: R${media_renda:.2f}")

        #Cidade com maior números de clientes.

        cidade_mais_clientes = df['Cidade'].value_counts().idxmax() #value_counts conta a quantos clientes tem em cada cidade. idxmax retorna o nome da cidade com maior quantidade de clientes.
        print(f"\nCidade com o maior número de clientes: {cidade_mais_clientes}")

        #Filtrar renda com valor específico.

        renda_minima = float(input("\nDigite a renda mínima para filtrar clientes: R$"))
        cliente_alta_renda = df[df['Renda']>renda_minima] #Irá filtrar clientes com renda maior que o valor digitado pelo usuario.
        print(f"\nCliente com renda acima de R${renda_minima:.2f}:")
        print(cliente_alta_renda)

except FileNotFoundError: #Se o arquivo não for encontrado inprimirá a mnesagem a seguir.
    print("Erro: O arquivo 'dados_clientes.csv' não foi encontrado.")

except KeyError as e: #Se a coluna não existir no arquivo, imprimir a mensagem a seguir.
    print(f"Erro: Coluna '{e}' não encontrada no arquivo CSV. Verifique o cabeçalho.")

except Exception as e: #Se ouver outro erro inesperado.
    print(f"Ocorreu um erro inesperado: {e}")