__all__ = ['novoJogo', 'rolaDado', 'pecasDic', 'vez', 'Captura','lastMoved']

import random
from view import tabuleiro
from tkinter import *

consecutivos = 0
lastMoved= None

class Peca:
    def __init__(self, casaX, casaY, tag):
        self.casaX = casaX
        self.casaY = casaY
        self.tag = tag

amarelo = Peca(14, 9, "amarelo")
vermelho1 = Peca(2, 7, "vermelho1")
vermelho2 = Peca(7, 2, "vermelho2")
verde = Peca(9, 2, "verde")
azul = Peca(7, 14, "azul")

pecasDic = [[vermelho1, vermelho2], [verde], [amarelo], [azul]]

#pecasDic = {
#  "vermelho": vermelho,
#  "verde": verde,
#  "amarelo": amarelo,
#  "azul": azul
#}

def novoJogo():
    global vez
    vez = random.randint(1,4)
    return vez

def rolaDado():
    global vez
    resultado = random.randint(1,6)
    check6(resultado)
    return resultado

def check6(resultado):
    global vez, consecutivos, lastMoved
    if resultado == 6:
        consecutivos += 1
        if consecutivos == 3:
            consecutivos = 0
            tabuleiro.c.move(lastMoved.tag, -55,-55) #precisa das contas certas
            if vez == 4:
                vez = 1
            else:
                vez += 1
        else:
            vez = vez
    else:
        consecutivos = 0
        if vez == 4:
            vez = 1
        else:
            vez += 1

def Captura(peao):
    global vez
    for jogadores in pecasDic:
        for peca in jogadores:
            if peao.casaX == peca.casaX and peao.casaY == peca.casaY:
                if peca not in pecasDic[vez-1]:
                    if (peca.casaX == 7 and peca.casaY == 2) or (peca.casaX == 14 and peca.casaY == 7) or (peca.casaX == 9 and peca.casaY == 14) or (peca.casaX == 2 and peca.casaY == 9):
                        return
                    else:
                        tabuleiro.c.move(peca.tag, 55, 55) #precisa das contas certas, mas já é um começo      
                        return
                else:
                    #barreira
                    return


                
    

        
    




