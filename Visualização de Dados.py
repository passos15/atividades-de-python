#Visualização de Dados
import pandas as pd
import matplotlib.pyplot as plt #O Matplotlib é uma das bibliotecas de visualização de dados mais utilizadas em Python, possibilitando a geração de gráficos de linha, de barra, entre outros.

#Dicionário.
data = {
"Nome": ['Ana', 'Bruno', 'Carlos', 'Eduardo', 'Fernanda', 'Gustavo'],
"Idade": [28, 35, 22, 40, 30, 25 ],
"Cidade": ['São Paulo', 'Rio de Janeiro', 'São Paulo', 'Belo Horizonte', 'Rio de Janeiro', 'São Paulo'],
"Renda": [5000.00, 7500.00, 3000.00, 9000.00, 6000.00, 4500.00] 
}

df_vis = pd.DataFrame(data) #O Pandas transforma o dicionário em uma tabela.

# Gráfico de barras
plt.figure(figsize=(10,6)) #Cria uma área para o gráfico.
df_vis['Cidade'].value_counts().plot(kind='bar', color= 'skyblue') #Conta quantas vezes cada cidade aparece. plot - cria o gráfico. kind='bar' - gráfico de barras. color='skyblue' - barras azuis claras.
plt.title("Número de clientes por cidade")
plt.xlabel('Cidade') #Nome do eixo X.
plt.ylabel('Número de clientes') #Nome do eixo Y.
plt.xticks(rotation=45) #Gira o nome das cidade em 45 graus.
plt.grid(axis='y', linestyle='--') #Adiciona linhas horizontais tracejadas.
plt.tight_layout() #Organiza o gráfico auttomaticamente para evitar cortes. 
plt.savefig('clientes_por_cidade.png') #Salva o gráfico no computador.
plt.show() #Mostra o gráfico.
print("Gráfico 'clientes_por_cidade.png' gerado.")