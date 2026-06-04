import random

class JogoDaForca:
    def __init__(self, palavras):
        self.palavras = palavras #Guarda a lista de palavras dentro do objeto.
        self.palavras_secreta = self._escolher_palavra()
        self.letras_corretas = [] #Cria uma lista vaziar e guardará as letras acertadas.
        self.letras_erradas = [] #Cria uma lista vaziar e guardará as letras erradas.
        self.tentativas_restantes = 6 #Número de partes do corpo da forca.
        self.estado_forca = [
            
"""
 +---+
 |   |
     |
     |
     |
     |
=========
""",
"""
 +---+
 |   |
 O   |
     |
     |
     |
=========
""",
"""
 +---+
 |   |
 O   |
 |   |
     |
     |
=========
""",
"""
 +---+
 |   |
 O   |
/|   |
     |
     |
=========
""",
"""
 +---+
 |   |
 O   |
/|\\  |
     |
     |
=========
""",
"""
 +---+
 |   |
 O   |
/|\\  |
/    |
     |
=========
""",
"""
 +---+
 |   |
 O   |  
/|\\  |
/ \\  |
     |
=========
"""
 ]
    def _escolher_palavra(self): #Cria um método para escolher uma palavra.
        return random.choice(self.palavras).upper() #Escolhe uma palavra aleatória.
    
    def _exibir_palavra_escondida(self): #Método que mostra os acertos do jogador.
        exibicao = ""
        for letra in self.palavras_secreta: #Percorre cada letra da palavra.
            if letra in self.letras_corretas: #Verifica se a letra já foi acertada.
                exibicao += letra + "" #Adiciona a letra na exibição.
            else:
                exibicao +="_" #Um exemplo de como ficará apos a formatação → P _ T _ _ _
        return exibicao.strip() #Retorna a palavra formatada.
        
    def _desenhar_forca(self): #Método responsável por mostrar o desenho.
        print(self.estado_forca[6-self.tentativas_restantes])

    def jogar(self):
        print("*************************************")
        print("       Bem-vindo ao Jogo da Forca!   ")
        print("*************************************")
        print("Adivinhe a palavra!")

        while self.tentativas_restantes > 0: #Enquanro o jogador ainda tiver tentativa o jogo continua rodando.
            self._desenhar_forca() #Mostra o estado atual da forca.
            print(f"palavra: {self._exibir_palavra_escondida()}")
            print(f"Letras erradas: {','.join(self.letras_erradas)}")
            print(f"Tentativas restantes: {self.tentativas_restantes}")

            tentativa = input("Digite uma letra: ").upper() #Pede uma letra ao jogador. '.upper' converte a letra digitada para maiúsculo.

            if len(tentativa) != 1 or not tentativa.isalpha(): #Verifica se o usuário digitou algo invalido.
                print("Entrada inválida. Digite apenas uma letra.")
                continue

            if tentativa in self.letras_corretas or tentativa in self.letras_erradas: #Verifica se a letra já foi usada.
                print(f"Você já tentou a letra '{tentativa}'.")
                continue

            if tentativa in self.palavras_secreta: #Verifica se a letra está na palavra secreta.
                self.letras_corretas.append(tentativa) #Guarda a letra na lista de acertos.
                print(f"Boa! A letra '{tentativa}' está na palavra.")
            else:
                self.letras_erradas.append(tentativa) #Guarda a letra na lista de erros.
                self.tentativas_restantes-=1 #Remove uma tentativa.
                print(f"Que pena! A letra '{tentativa}' não está na palavra.")

            if "_" not in self._exibir_palavra_escondida(): #Verifica se ainda existe algum expaço, se não existir todas as letras foram descobertas.
                print("\nParabéns! Você adivinhou a palavra!")
                print(f"A palavra era: {self.palavras_secreta}")
                self._desenhar_forca() #mostra a forca pela última vez.
                break
            else:
                self._desenhar_forca() 
                print("\nVocê perdeu!")
                print(f"A palavra secreta era: {self.palavras_secreta}")

palavras_forca = ["PYTHON", "PROGRAMACAO", "DESENVOLVIMENTO", "COMPUTADOR", "ALGORITMO", "INTELIGENCIA"] #Palavras que poderam aparecer na forca.
jogo = JogoDaForca(palavras_forca) 
jogo.jogar()