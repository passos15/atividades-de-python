n = int(input('Digite o número desejado para a tabuada: '))
for i in range(1, 11):
    print(f'{n} x {i} = {n * i}')

#A cada volta do laço o "i", assume um valor diferente.
# O range(1, 11) diz: "comece no 1 e pare antes de chegar no 11". Ou seja, ele vai de 1 até 10.
# O for é um tipo de laço de repetição que é usado para repetir um bloco de código um número específico de vezes.
# # O print(f'{n} x {i} = {n * i}') é como um "cartaz mágico". Ele pega o número que você digitou (n), o número atual do loop (i) e calcula a multiplicação (n * i).