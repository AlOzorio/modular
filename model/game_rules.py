__all__ = ['novoJogo', 'rolaDado', 'pecasDic', 'vez', 'Captura','lastMoved', 'check5']

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
    def __init__(self, casaX, casaY, tag, casasAndadas, posIni, cor):
        self.casaX = casaX
        self.casaY = casaY
        self.tag = tag
        self.casasAndadas = casasAndadas
        self.posIni = posIni
        self.cor = cor

vermelho1 = Peca(1.85, 1.85, "vermelho1", 0, [1.85, 1.85], 0)
vermelho2 = Peca(4.78, 1.85, "vermelho2", 0, [4.78, 1.85], 0)
vermelho3 = Peca(1.85, 4.78, "vermelho3", 0, [1.85, 4.78], 0)
vermelho4 = Peca(4.78, 4.78, "vermelho4", 0, [4.78, 4.78], 0)
verde1 = Peca(10.85, 1.85, "verde1", 0, [10.85, 1.85], 1) 
verde2 = Peca(13.78, 1.85, "verde2", 0, [13.78, 1.85], 1) 
verde3 = Peca(10.85, 4.78, "verde3", 0, [10.85, 4.78], 1) 
verde4 = Peca(13.78, 4.78, "verde4", 0, [13.78, 4.78], 1) 
amarelo1 = Peca(10.85, 10.85, "amarelo1", 0, [10.85, 10.85], 2) 
amarelo2 = Peca(13.78, 10.85, "amarelo2", 0, [13.78, 10.85], 2) 
amarelo3 = Peca(10.85, 13.78, "amarelo3", 0, [10.85, 13.78], 2) 
amarelo4 = Peca(13.78, 13.78, "amarelo4", 0, [13.78, 13.78], 2) 
azul1 = Peca(1.85, 10.85, "azul1", 0, [1.85, 10.85], 3) 
azul2 = Peca(4.78, 10.85, "azul2", 0, [4.78, 10.85], 3) 
azul3 = Peca(1.85, 13.78, "azul3", 0, [1.85, 13.78], 3) 
azul4 = Peca(4.78, 13.78, "azul4", 0, [4.78, 13.78], 3) 

pecasDic = [[vermelho1, vermelho2, vermelho3, vermelho4], [verde1, verde2, verde3, verde4], [amarelo1, amarelo2, amarelo3, amarelo4], [azul1, azul2, azul3, azul4]]


def novoJogo():
    global vez
    vez = random.randint(1,4)
    return vez

def rolaDado():
    global vez
    resultado = random.randint(1,6)
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

def check5(resultado):
    global vez
    cores = ['red4', 'dark green', 'goldenrod1', 'midnight blue']
    if resultado == 5:
        for peca in pecasDic[vez - 1]:
            if peca.casaX == peca.posIni[0] and peca.casaY == peca.posIni[1]:
                if vez == 2:                    
                    movX = 9 
                    movY = 2
                     
                if vez == 3: 
                    movX = 14 
                    movY = 9
                     
                if vez == 4: 
                    movX = 7 
                    movY = 14
                     
                if vez == 1:
                    movX = 2 
                    movY = 7
                
                tabuleiro.c.delete(peca.tag)
                peca.casaX = movX
                peca.casaY = movY
                tabuleiro.c.create_oval((movX-1) * 55 + 15, (movY-1) * 55 + 15, 55*(movX-1) + 60, 55*(movY-1) + 60, outline='gray4',width=2,fill=cores[vez - 1], tag = peca.tag) 
                if vez == 4:
                    vez = 1
                else:
                    vez += 1
                tabuleiro.Enable()
                break
    else:
        for peca in pecasDic[vez - 1]:
            if peca.casaX != peca.posIni[0] and peca.casaY != peca.posIni[1]:
                return
            else:
                if vez == 4:
                    vez = 1
                else:
                    vez += 1
                tabuleiro.Enable()
                break

def Captura(peao):
    global vez
    cores = ['red4', 'dark green', 'goldenrod1', 'midnight blue']
    for jogadores in pecasDic:
        for peca in jogadores:
            if peao.casaX == peca.casaX and peao.casaY == peca.casaY:
                if peca not in pecasDic[vez-1]:
                    if (peca.casaX == 7 and peca.casaY == 2) or (peca.casaX == 14 and peca.casaY == 7) or (peca.casaX == 9 and peca.casaY == 14) or (peca.casaX == 2 and peca.casaY == 9):
                        return
                    else:
                        tabuleiro.c.delete(peca.tag)
                        tabuleiro.c.create_oval((peca.posIni[0]-1) * 55 + 15, (peca.posIni[1]-1) * 55 + 15, 55*(peca.posIni[0]-1) + 60, 55*(peca.posIni[1]-1) + 60, outline='gray4',width=2,fill=cores[peca.cor], tag = peca.tag)  
                        peca.casaX = peca.posIni[0]
                        peca.casaY = peca.posIni[1]
                        return



                
    

        
    




