#Analise de Dados Simples (CSV)
import csv #É uma biblioteca que armazana arquivos em formato de tabela.

def analisar(vendas):
    total = 0 #Variável que irá armazana o valor total de todas as vendas. 
    produtos = {} #Dicionário que será usado para guardar a quantidade total que foi vendido de cada produto. 

    try: #Tenta execultar o codigo, se ouver erro pulará para except. 
        with open(vendas, 'r', encoding = 'utf-8') as arquivo: #Abre o arquivo CSV no modo leitura e com codificação UTF-8(lê o texto, evitando problemas com acentos).
            leitor = csv.DictReader(arquivo) #É uma função que lê um arquivo e transforma linhas em dicionário.

            for linha in leitor: #Percorre cada linha do arquivo.
                produto = linha['produto'] 
                quantidade = int(linha['quantidade'])
                preco = float(linha['preco'])
                #Extrai as informações das respectivas colunas.

                total += quantidade*preco #Multiplica a quantidade pelo preço e o resuldado será o total de vendas.
                produtos[produto] = produtos.get(produto, 0) + quantidade #Atualiza a quantidade total vendida de um produto no diiconario.

                if produtos:
                    produtos_mais_vendidos = max(produtos, kay= produtos.get) #Encontra o produto com a maior quantidade vendida no dicionário.
                    print(f"\n---Análise de vendas---")
                    print(f"Total de vendas: R${total:.2f}")
                    print(f"Produto mais vendido: {produtos_mais_vendidos}({produtos[produtos_mais_vendidos]} unidades)")
                    #Exibe o nome do produto mais vendido e a quantidade total vendida desse produto.

                else:
                    print("Nenhum dado de vendas encontrado.")

    except FileNotFoundError: #Ocorre quando o arquivo não existe no caminho especificado.
        print(f"Erro: O arquivo'{vendas}' não foi encontrado")
    
    except KeyError as e: #Ocorre quando você tenta acessar uma chave que não existe em um dicionário.
        print(f"Erro: Coluna '{e}' não encontrada no arquivo CSV. Verifique o cabeçalho.")

    except ValueError as e: #Ocorre quando uma conversão de tipo falha
        print(f"Erro de conversão de dados: {e}. Verifique os valores numéricos no CSV.")
    
    except Exception as e: #Captura qualquer outro erro que não foi tratado pelos except anteriores.
        print(f"Ocorreu um erro inesperado: {e}")

analisar('vendas.csv')