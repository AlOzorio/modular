

class Jogador:

    def __init__(self, nome, cor):
        self.nome = nome
        self.cor = cor
        self.pecasFinalizadas = 0
    
    def testeVencedor(self):
        return self.pecasFinalizadas == 4

def criaJogadores():
    vetorJogadores = []
    
    for i in range(2):
        print("Qual o nome do jogador " + str(i + 1) + "?")
        nome = input()

        print("Qual a cor escolhida por " + nome + "?")
        cor = input()

        jogador = Jogador(nome, cor)

        vetorJogadores.append(jogador)

