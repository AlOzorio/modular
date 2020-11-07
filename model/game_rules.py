__all__ = ['novoJogo', 'rolaDado', 'pecasDic', 'vez']

import random

consecutivos = 0

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
    global vez, consecutivos
    if resultado == 6:
        consecutivos += 1
        if consecutivos == 3:
            consecutivos = 0
            #retorna peão para o início
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

        
    




