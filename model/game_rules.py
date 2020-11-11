__all__ = ['novoJogo', 'rolaDado', 'pecasDic', 'vez', 'Captura','lastMoved']

import random
from view import tabuleiro
from tkinter import *

consecutivos = 0
lastMoved= None

class Peca:
    def __init__(self, casaX, casaY, tag, posIni):
        self.casaX = casaX
        self.casaY = casaY
        self.tag = tag
        self.posIni = posIni

vermelho1 = Peca(1.85, 1.85, "vermelho1", [1.85, 1.85])
vermelho2 = Peca(4.78, 1.85, "vermelho2", [4.78, 1.85])
vermelho3 = Peca(1.85, 4.78, "vermelho3", [1.85, 4.78])
vermelho4 = Peca(4.78, 4.78, "vermelho4", [4.78, 4.78])
verde1 = Peca(9, 1.85, "verde1", [10.85, 1.85])
verde2 = Peca(9, 1.85, "verde2", [13.78, 1.85])
verde3 = Peca(9, 4.78, "verde3", [10.85, 4.78])
verde4 = Peca(9, 4.78, "verde4", [13.78, 4.78])
amarelo1 = Peca(14, 9, "amarelo1", [10.85, 10.85])
amarelo2 = Peca(14, 9, "amarelo2", [13.78, 10.85])
amarelo3 = Peca(14, 9, "amarelo3", [10.85, 13.78])
amarelo4 = Peca(14, 9, "amarelo4", [13.78, 13.78])
azul1 = Peca(7, 14, "azul1", [1.85, 10.85])
azul2 = Peca(7, 14, "azul2", [4.78, 10.85])
azul3 = Peca(7, 14, "azul3", [1.85, 13.78])
azul4 = Peca(7, 14, "azul4", [4.78, 13.78])

pecasDic = [[vermelho1, vermelho2, vermelho3, vermelho4], [verde1, verde2, verde3, verde4], [amarelo1, amarelo2, amarelo3, amarelo4], [azul1, azul2, azul3, azul4]]

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
    tabuleiro.check5(resultado, vez)
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


                
    

        
    




