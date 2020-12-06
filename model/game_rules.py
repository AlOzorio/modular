__all__ = ['novoJogo', 'rolaDado', 'pecasDic', 'vez', 'Captura','lastMoved', 'check5', 'CheckBarreira', 'CheckSupremo', 'CheckWin', 'SomaPontos', 'CheckAbrigo', 'check6Barreira']

import random
from view import tabuleiro
from tkinter import *
from tkinter import messagebox

consecutivos = 0
abrigos = [[7,2], [14, 7], [9, 14], [2, 9], [2, 7], [9, 2], [14, 9], [7, 14]]

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

vermelho1 = Peca(1.85, 1.85, "vermelho1", -1, [1.85, 1.85], 0)
vermelho2 = Peca(4.78, 1.85, "vermelho2", -1, [4.78, 1.85], 0)
vermelho3 = Peca(1.85, 4.78, "vermelho3", -1, [1.85, 4.78], 0)
vermelho4 = Peca(4.78, 4.78, "vermelho4", -1, [4.78, 4.78], 0)
verde1 = Peca(10.85, 1.85, "verde1", -1, [10.85, 1.85], 1) 
verde2 = Peca(13.78, 1.85, "verde2", -1, [13.78, 1.85], 1) 
verde3 = Peca(10.85, 4.78, "verde3", -1, [10.85, 4.78], 1) 
verde4 = Peca(13.78, 4.78, "verde4", -1, [13.78, 4.78], 1) 
amarelo1 = Peca(10.85, 10.85, "amarelo1", -1, [10.85, 10.85], 2) 
amarelo2 = Peca(13.78, 10.85, "amarelo2", -1, [13.78, 10.85], 2) 
amarelo3 = Peca(10.85, 13.78, "amarelo3", -1, [10.85, 13.78], 2) 
amarelo4 = Peca(13.78, 13.78, "amarelo4", -1, [13.78, 13.78], 2) 
azul1 = Peca(1.85, 10.85, "azul1", -1, [1.85, 10.85], 3) 
azul2 = Peca(4.78, 10.85, "azul2", -1, [4.78, 10.85], 3) 
azul3 = Peca(1.85, 13.78, "azul3", -1, [1.85, 13.78], 3) 
azul4 = Peca(4.78, 13.78, "azul4", -1, [4.78, 13.78], 3) 

pecasDic = [[vermelho1, vermelho2, vermelho3, vermelho4], [verde1, verde2, verde3, verde4], [amarelo1, amarelo2, amarelo3, amarelo4], [azul1, azul2, azul3, azul4]]

def CheckWin():
    global vez
    fim = 0
    for item in pecasDic[vez-1]:
        if item.casasAndadas == 58:
            fim += 1
        if fim == 4:
            tabuleiro.lancaDado.configure(state = DISABLED)
            tabuleiro.Dado1.configure(state = DISABLED)
            tabuleiro.Dado2.configure(state = DISABLED)
            tabuleiro.Dado3.configure(state = DISABLED)
            tabuleiro.Dado4.configure(state = DISABLED)
            tabuleiro.Dado5.configure(state = DISABLED)
            tabuleiro.Dado6.configure(state = DISABLED)
            return True
    return False
            
def SomaPontos():
    soma = [['Vermelho: ',0], ['Verde: ', 0], ['Amarelo: ', 0], ['Azul: ', 0]]
    
    for jogador in pecasDic:
        for peca in jogador:
            soma[peca.cor][1] += peca.casasAndadas
            
    soma.sort(reverse = True, key = lambda x: x[1])
    
    msg = '\n 1º - ' + soma[0][0] + str(soma[0][1]) + '\n 2º - ' +soma[1][0] + str(soma[1][1]) + '\n 3º - ' + soma[2][0] + str(soma[2][1]) + '\n 4º - ' + soma[3][0] + str(soma[3][1])
    messagebox.showinfo(title='Resultado',message=msg, icon='info')


def CheckAbrigo(peca, resultado):
    global vez
    cont = 0
    
    if vez == 1:
        caminho = caminhoVermelho
        
    elif vez == 2:
        caminho = caminhoVerde
        
    elif vez == 3:
        caminho = caminhoAmarelo
        
    elif vez == 4:
        caminho = caminhoAzul
        
    if caminho[peca.casasAndadas + resultado] in abrigos:
        abrigoAtual = caminho[peca.casasAndadas + resultado]
        for jogadores in pecasDic:
            for peca in jogadores:
                if peca.casaX == abrigoAtual[0] and peca.casaY == abrigoAtual[1]:
                    cont += 1
    if cont >= 2:
        return True
    
    return False
    

def CheckSupremo(resultado):
    global vez
    foraBarreira = 0
    foraAbrigo = 0
    
    for item in pecasDic[vez - 1]:
        if item.casaX != item.posIni[0] or item.casaY != item.posIni[1]:
            foraBarreira += 1
            foraAbrigo += 1
            if CheckBarreira(item, resultado) == True:
                foraBarreira -= 1
                
            if CheckAbrigo(item, resultado) == True:
                foraAbrigo -= 1
                
    if foraBarreira == 0 or foraAbrigo == 0:
        return True
    return False

def CheckBarreira(peca, resultado):
    global vez, caminhoVermelho, caminhoVerde, caminhoAmarelo, caminhoAzul
    cont = 0
    
    if vez == 1:
        caminho = caminhoVermelho
        
    elif vez == 2:
        caminho = caminhoVerde
        
    elif vez == 3:
        caminho = caminhoAmarelo
        
    elif vez == 4:
        caminho = caminhoAzul
        
    if peca.casasAndadas + resultado + 1 < 58:
        for i in range(peca.casasAndadas + 1, peca.casasAndadas + resultado + 1):
            for container in pecasDic:
                for item in container:
                    if item.casaX == caminho[i][0] and item.casaY == caminho[i][1]:
                        cont += 1
                if cont >= 2:
                    return True
                cont = 0
    return False
    
    

def novoJogo():
    global vez
    vez = random.randint(1,4)
    return vez

def rolaDado():
    global vez
    resultado = random.randint(1,6)
    return resultado

def check6Barreira(n):
    global vez
    cont = 0
    if n == 6:
        for peca1 in pecasDic[vez - 1]:
            for peca2 in pecasDic[vez - 1]:
                if peca1.tag != peca2.tag and peca1.casasAndadas == peca2.casasAndadas and peca1.casasAndadas != -1 and peca2.casasAndadas != -1:
                    if cont == 0:
                        pecaToMove = peca1
                        cont += 1
                    else:
                        if pecaToMove.casasAndadas < peca1.casasAndadas:
                            pecaToMove = peca1
                            cont += 1
                    
    posicoes = tabuleiro.MovePeca(pecaToMove, n)
    if posicoes != [pecaToMove.casaX, pecaToMove.casaY]:
        tabuleiro.c.move(pecaToMove.tag, (posicoes[0] - pecaToMove.casaX) * 55, (posicoes[1] - pecaToMove.casaY) * 55)
        pecaToMove.casaX = posicoes[0]
        pecaToMove.casaY = posicoes[1]
        lastMoved = pecaToMove
        Captura(pecaToMove)
    check6(n)
    tabuleiro.Enable()
    
    

def check6(resultado):
    global vez, consecutivos, lastMoved
    if resultado == 6:
        consecutivos += 1
        if consecutivos == 3:
            consecutivos = 0
            if lastMoved.casasAndadas < 58:
                tabuleiro.c.move(lastMoved.tag, (lastMoved.posIni[0]-lastMoved.casaX)*55, (lastMoved.posIni[1]-lastMoved.casaY)*55)
                lastMoved.casaX = lastMoved.posIni[0]
                lastMoved.casaY = lastMoved.posIni[1]
                lastMoved.casasAndadas = -1
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
    temGente = False
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
                
                for peca2 in pecasDic[vez - 1]:
                    if peca2.casaX == movX and peca2.casaY == movY:
                        temGente = True
                
                if temGente == False:
                    tabuleiro.c.delete(peca.tag)
                    peca.casaX = movX
                    peca.casaY = movY
                    peca.casasAndadas = 0
                    tabuleiro.c.create_oval((movX-1) * 55 + 15, (movY-1) * 55 + 15, 55*(movX-1) + 60, 55*(movY-1) + 60, outline='gray4',width=2,fill=cores[vez - 1], tag = peca.tag)
                    Captura(peca)
                    
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
                    print(vez)
                    if (peca.casaX == 7 and peca.casaY == 2) or (peca.casaX == 14 and peca.casaY == 7) or (peca.casaX == 9 and peca.casaY == 14) or (peca.casaX == 2 and peca.casaY == 9):
                       return
                    elif peca.cor == 0 and peca.casaX == 2 and peca.casaY == 7:
                        return
                    elif peca.cor == 1 and peca.casaX == 9 and peca.casaY == 2:
                        return
                    elif peca.cor == 2 and peca.casaX == 14 and peca.casaY == 9:
                        return
                    elif peca.cor == 3 and peca.casaX == 7 and peca.casaY == 14:
                        return
                    else:
                        tabuleiro.c.delete(peca.tag)
                        tabuleiro.c.create_oval((peca.posIni[0]-1) * 55 + 15, (peca.posIni[1]-1) * 55 + 15, 55*(peca.posIni[0]-1) + 60, 55*(peca.posIni[1]-1) + 60, outline='gray4',width=2,fill=cores[peca.cor], tag = peca.tag)  
                        peca.casaX = peca.posIni[0]
                        peca.casaY = peca.posIni[1]
                        peca.casasAndadas = -1
                        return



                
    

        
    




