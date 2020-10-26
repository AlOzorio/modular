__all__ = ['novoJogo', 'rolaDado']

import random

consecutivos = 0

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




