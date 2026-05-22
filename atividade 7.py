#contador de vogais
def contador_vogais(texto): #O def é usado para criar uma função, 'contador_vogais' é o nome que foi definido para a função.
    vogais = 'aeiouAEIOU' #Uma variavel criada para o programa saber quais letras devem ser contadas.
    contador = 0 #Variavel que contara as vogais, começa valendo 0, quando o programa receber a frase começara a contar.
    for letra in texto: #Um loop que vai percorrer letra por letra da frase.
        if letra in vogais: #Verifica se alguma das letras verificadas pelo for é uma vogal.
            contador =+ #Toda vez que uma vogal for encontrada o contador adicionara um.
    return contador #Quando todas as letras são verificadas é retornado a quantidade de vogais encontradas.
frese = input("Digite uma frase: ")
num = contador_vogais(frese) #A função é chamada e a frase é enviada para a função.
print(f"A frase possui {num} vogais.")