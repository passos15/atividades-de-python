#Gerador de senhas
import random #É uma bibliboteca que trabalha com aleatoriedade.
import string #É uma biblioteca que possui um conjunto variado de caracteres prontos.

def gerar_senha(tamanho, 
                incluir_maiusculas=True, 
                incluir_minuscula=True, 
                incluir_numeros=True, 
                incluir_especiais=True
                ):
    #Tamanho é um parametro que receberá o tamanho da senha escolhida pelo usuario.
    #A seguir são os tipos de caracteristicas que poderam ser usadas na senha.

    caracteres = '' #Uma variavel que irá guardar todas as caracteris da senha.
    if incluir_maiusculas: caracteres += string.ascii_uppercase
    if incluir_minuscula: caracteres += string.ascii_lowercase
    if incluir_numeros: caracteres += string.digits
    if incluir_especiais: caracteres += string.punctuation
    #Caso o usuario escolher alguma das caracteristicas será a variavel.

    if not caracteres: #Se o usuario responder não a todas os caracteres retornara um erro.
        return"Erro:Nenhuma opção de caractere selecionada."
    
    senha = ''.join(random.choice(caracteres) for i in range (tamanho))
    #O join é responsavel por juntar todas as caracteristicas da senha.
    #random.choice(caracteres) escolhe um caractere aleatorio.
    #for i in range(tamanho) faz o codigo se repetir ate atingir a quantidade decaractere escolhida pelo usuario.
    return senha


tam = int(input("Tamanho da senha: "))

mai = input("Incluir maiúsculas? (s/n): ").lower()=='s' #O lower é usado para transformar letras encritas pelo usuario em minuscula.
min = input("Incluir minúsculas? (s/n): ").lower()=='s'
num = input("Incluir números? (s/n): ").lower()=='s'
esp = input("Incluir especiais? (s/n): ").lower()=='s'

senha_gerada = gerar_senha(tam, mai, min, num, esp) #Aqui é a função é executada.
print(f"Senha gerada: {senha_gerada}")