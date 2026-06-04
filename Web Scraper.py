#Web Scraper
import requests #Requests é a maneira mais convencional de lidar com solicitações Web em Python.
from bs4 import BeautifulSoup #Instrução padrão do Python para importar a classe principal da biblioteca Beautiful Soup 4, que é utilizada para fazer a leitura e a análise de documentos HTML e XML.

def extrair_titulos_noticias(url, nome_arquivo='noticias.txt'): #url - é o endereço do site, nome_arquivo - é o arquivo onde os títulos serão salvos.
    
    try:
        response = requests.get(url) #O conteúdo da página será guardado em response.
        response.raise_for_status() #Verifica se a página foi carregada corretamente.

        soup = BeautifulSoup(response.text,'html.parser') #BeautifulSoup é uma biblioteca usada em Python para extrair dados de arquivos HTML e XML.
        #↑↑↑Faz a leitura do HTML e constrói um objeto soup, que possibilita a navegação e a busca de elementos no código.

        titulos = soup.find_all('h2') #Busca todos os elementos <h2> no HTML.

        with open(nome_arquivo, 'w', encoding='utf-8') as f:
            for titulo in titulos:
                texto_titulo = titulo.get_text(strip=True) #Extrai o texto do elemento HTML, removendo espaços em branco.
                f.write(texto_titulo + '\n') #Escreve cada título em uma linha do arquivo.
        print(f"Títitulo de notícias extraidos e salvos em '{nome_arquivo}'.")

    except requests.exceptions.RequestException as e: #Captura erros relacionados à requisição HTTP.
        print(f"Erro de conexão ou HTTP: {e}") 
    
    except Exception as e:  #Captura qualquer outro erro inesperado.
        print(f"Ocorreu um erro: {e}")

url_noticias = "https://www.bnews.com.br/"
extrair_titulos_noticias(url_noticias)