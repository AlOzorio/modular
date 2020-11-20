__all__ = ['novoJogo', 'rolaDado', 'pecasDic', 'vez', 'Captura','lastMoved']

import random
from view import tabuleiro
from tkinter import *

consecutivos = 0
lastMoved= None

caminhoVermelho = [[2, 7],[3, 7],[4, 7],[5, 7],[6, 7],[7, 6],[7, 5],[7, 4],[7, 3],[7, 2],[7, 1],[8, 1],[9, 1],[9, 2],[9, 3],[9, 4],[9, 5],[9, 6],[10, 7],[11, 7],[12, 7],[13, 7],[14, 7],[15, 7],[15, 8],[15, 9],[14, 9],[13, 9],[12, 9],[11, 9],[10 , 9],[9, 10],[9, 11],[9, 12],[9, 13],[9, 14],[9, 15],[8, 15],[7, 15],[7, 14],[7, 13],[7, 12],[7, 11],[7, 10],[6, 9],[5, 9],[4, 9],[3, 9],[2, 9],[1, 9],[1, 8],[1, 7],[2, 7],[2, 8],[3, 8],[4, 8],[5, 8],[6, 8],[7, 8]]
caminhoVerde = [[9, 2],[9, 3],[9, 4],[9, 5],[9, 6],[10, 7],[11, 7],[12, 7],[13, 7],[14, 7],[15, 7],[15, 8],[15, 9],[14, 9],[13, 9],[12, 9],[11, 9],[10 , 9],[9, 10],[9, 11],[9, 12],[9, 13],[9, 14],[9, 15],[8, 15],[7, 15],[7, 14],[7, 13],[7, 12],[7, 11],[7, 10],[6, 9],[5, 9],[4, 9],[3, 9],[2, 9],[1, 9],[1, 8],[1, 7],[2, 7],[3, 7],[4, 7],[5, 7],[6, 7],[7, 6],[7, 5],[7, 4],[7, 3],[7, 2],[7, 1],[8, 1],[9, 1],[9, 2],[8, 2],[8, 3],[8, 4],[8, 5],[8, 7],[8, 7]]
caminhoAmarelo = [[14, 9],[13, 9],[12, 9],[11, 9],[10 , 9],[9, 10],[9, 11],[9, 12],[9, 13],[9, 14],[9, 15],[8, 15],[7, 15],[7, 14],[7, 13],[7, 12],[7, 11],[7, 10],[6, 9],[5, 9],[4, 9],[3, 9],[2, 9],[1, 9],[1, 8],[1, 7],[2, 7],[3, 7],[4, 7],[5, 7],[6, 7],[7, 6],[7, 5],[7, 4],[7, 3],[7, 2],[7, 1],[8, 1],[9, 1],[9, 2],[9, 3],[9, 4],[9, 5],[9, 6],[10, 7],[11, 7],[12, 7],[13, 7],[14, 7],[15, 7],[15, 8],[15, 9],[14, 9],[14, 8],[13, 8],[12, 8],[11, 8],[10, 8],[9, 8]]
caminhoAzul = [[7, 14],[7, 13],[7, 12],[7, 11],[7, 10],[6, 9],[5, 9],[4, 9],[3, 9],[2, 9],[1, 9],[1, 8],[1, 7],[2, 7],[3, 7],[4, 7],[5, 7],[6, 7],[7, 6],[7, 5],[7, 4],[7, 3],[7, 2],[7, 1],[8, 1],[9, 1],[9, 2],[9, 3],[9, 4],[9, 5],[9, 6],[10, 7],[11, 7],[12, 7],[13, 7],[14, 7],[15, 7],[15, 8],[15, 9],[14, 9],[13, 9],[12, 9],[11, 9],[10 , 9],[9, 10],[9, 11],[9, 12],[9, 13],[9, 14],[9, 15],[8, 15],[7, 15],[7, 14],[8, 14],[8, 13],[8, 12],[8, 11],[8, 10],[8, 9]]

class Peca:
    def __init__(self, casaX, casaY, tag, casasAndadas, posIni):
        self.casaX = casaX
        self.casaY = casaY
        self.tag = tag
        self.casasAndadas = casasAndadas
        self.posIni = posIni

vermelho1 = Peca(1.85, 1.85, "vermelho1", 0, [1.85, 1.85])
vermelho2 = Peca(4.78, 1.85, "vermelho2", 0, [4.78, 1.85])
vermelho3 = Peca(1.85, 4.78, "vermelho3", 0, [1.85, 4.78])
vermelho4 = Peca(4.78, 4.78, "vermelho4", 0, [4.78, 4.78])
verde = Peca(9, 2, "verde", 0, [9, 2])
amarelo = Peca(14, 9, "amarelo", 0, [14,9])
azul = Peca(7, 14, "azul", 0, [7, 14])

pecasDic = [[vermelho1, vermelho2,vermelho3,vermelho4], [verde], [amarelo], [azul]]

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
    #check6(resultado)
    return resultado

def check6(resultado):
    global vez, consecutivos, lastMoved
    if resultado == 6:
        consecutivos += 1
        if consecutivos == 3:
            consecutivos = 0
            tabuleiro.c.move(lastMoved.tag, (lastMoved.posIni[0]-lastMoved.casaX)*55, (lastMoved.posIni[1]-lastMoved.casaY)*55) #precisa das contas certas
            lastMoved.casaX = lastMoved.posIni[0]
            lastMoved.casaY = lastMoved.posIni[1]
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
                        tabuleiro.c.move(peca.tag, (peca.casaX-peca.posIni[0])*55, (peca.casaY-peca.posIni[1])*55) #precisa das contas certas, mas já é um começo      
                        peca.casaX = peca.posIni[0]
                        peca.casaY = peca.posIni[1]
                        return
                else:
                    #barreira
                    return


                
    

        
    




