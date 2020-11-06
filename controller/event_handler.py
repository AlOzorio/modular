from tkinter import *
from model import game_rules

def click(event):
    x = event.x
    y = event.y
    
    casaX = ((x - 10) // 55) + 1
    casaY = ((y - 10) // 55) + 1
    
    current = game_rules.vez - 1
    
    for peca in game_rules.pecasDic[current]:
        if peca.casaX == casaX and peca.casaY == casaY:
            print(True)
            
    
