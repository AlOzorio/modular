__all__ = ['click', 'pos']

from tkinter import *
from model import game_rules
from view import tabuleiro

pos = [None, None]

def click(event):
    global pos
    x = event.x
    y = event.y
    
    casaX = ((x - 10) // 55) + 1
    casaY = ((y - 10) // 55) + 1
    
    current = game_rules.vez - 1
    
    for peca in game_rules.pecasDic[current]:
        if peca.casaX == casaX and peca.casaY == casaY:
            pos = [casaX, casaY]
            tabuleiro.CheckPeca(peca)
            return True
    pos = [None, None]
    tabuleiro.CheckPeca(peca)
    return False
    

