#Calculando fatoral
def fatorial(n): #O def é usado para definir uma função.
    if n == 0 or n == 1:
        return 1 #Se o número for igual a 0 ou 1, retornará para 1; assim, o código não rodará sem parar.
    else: #Se o número for acima de 1, o fatorial será calculado e imprimido return.
          return n * fatorial(n-1)
    
numero = int(input("Digite um número inteiro positivo para calcular o fatorial: "))
#O if  servirá para mostrar que números negativos não tem fatorial.
if numero <0:
    print("Fatorial não é definido para números negativos.")
#O else mostrará o resultado da equação.
else:
    print(f"O fatorial de um {numero} é {fatorial(numero)}.")