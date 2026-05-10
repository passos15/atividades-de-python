#contador de vogais.
v = input("Digite uma frase: ")
contador = 0
vogais = "aeiouAEIOU"

for letra in v:
    if letra in vogais:
        contador +=1

print(f"A quantidade de vogais é: {contador}")