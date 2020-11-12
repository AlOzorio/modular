__all__ = ['c']

from tkinter import *
from model import game_rules
from controller import event_handler

xis = 0
root = Tk()
root.geometry('1170x845+410+130')
root.title('Ludo')
c = Canvas(root, width=1170, height=845)
c.bind('<ButtonRelease-1>', event_handler.click)
c.pack()
bigRectangle = c.create_rectangle(10, 10, 835,835,outline='gray4',width=2)

def check5(dado, vez):
#    print(vez)
    if dado == 5:
        if game_rules.pecasDic[vez - 1][0]:
            if vez == 2:
                movX = 9
                movY = 2
#                print("A")
                
            if vez == 3:
                movX = 14
                movY = 9
#                print("B")
                
            if vez == 4:
                movX = 7
                movY = 14
#                print("C")
                
            if vez == 1:
                movX = 2
                movY = 7
#                print("D")
        c.delete(game_rules.pecasDic[vez - 1][0].tag)
        c.create_oval((movX-1) * 55 + 15, (movY-1) * 55 + 15, 55*(movX-1) + 60, 55*(movY-1) + 60, outline='gray4',width=2,fill=cores[vez - 1], tag = game_rules.pecasDic[vez - 1][0].tag)
#            c.move(game_rules.pecasDic[vez - 1][0].tag, movX * 55 - game_rules.pecasDic[vez - 1][0].casaX * 55, game_rules.pecasDic[vez - 1][0].casaY * 55 - movY * 55)

        
def CheckPeca():
    global n
    if(event_handler.pos == [None, None]):
        print(False)
    else:
        for peca in game_rules.pecasDic[game_rules.vez - 2]:
            print(peca.casaX)
            print(event_handler.pos[0])
            if peca.casaX == event_handler.pos[0] and peca.casaY == event_handler.pos[1]:
                print('entrou')
                peca.posicoes = MovePeca(peca,n)
                c.move(peca.tag, peca.posicoes[0] * 55, peca.posicoes[1] * 55)
                peca.casaX += peca.posicoes[0]
                peca.casaY += peca.posicoes[1]
                game_rules.lastMoved = peca
                game_rules.Captura(peca)
        print(True)


def MovePeca(peca, dado):
    moveX = 0
    moveY = 0
        
    if(peca.casaX <= 6 and peca.casaY == 7):
        moveX = dado
        if(peca.casaX + dado > 6):
            moveX = 6 - peca.casaX + 1
            moveY = 6 - peca.casaX - dado
    elif(peca.casaX == 9 and peca.casaY <= 6):
        moveY = dado
        if(peca.casaY + dado > 6):
            moveY = 6 - peca.casaY + 1
            moveX = peca.casaY + dado - 6
    elif(peca.casaX >= 10 and peca.casaY == 9):
        moveX = -dado
        if(peca.casaX - dado < 10):
            moveX = 10 - peca.casaX - 1
            moveY = dado + moveX + 1
    elif(peca.casaX == 7 and peca.casaY >= 10):
        moveY = -dado
        if(peca.casaY - dado < 10):
            moveX = - 10 + peca.casaY - dado 
            moveY = - peca.casaY + 10 - 1
    elif(peca.casaX == 7 and peca.casaY <= 6):
        moveY = -dado
        if(peca.casaY - dado < 1):
            moveY = -peca.casaY + 1
            moveX = dado + moveY
            if(moveX > 2):
                moveY += moveX - 2
                moveX = 2
    elif(peca.casaX >= 10 and peca.casaY == 7):
        moveX = dado
        if(peca.casaX + dado > 15):
            moveX = 6 - (peca.casaX - 9)
            moveY = dado - moveX
            if(moveY > 2):
                moveX -= moveY - 2
                moveY = 2
    elif(peca.casaX == 9 and peca.casaY >= 10):
        moveY = dado
        if(peca.casaY + dado > 15):
            moveY = 6 - (peca.casaY - 9)
            moveX = -(dado - moveY)
            if(moveX < -2):
                moveY += moveX + 2
                moveX = -2
    elif(peca.casaX <= 6 and peca.casaY == 9):
        moveX = -dado
        if(peca.casaX - dado < 1):
            moveX = -peca.casaX + 1
            moveY = - dado - moveX
            if(moveY < -2):
                moveX -= moveY + 2
                moveY = -2
    elif(peca.casaX == 8 and peca.casaY == 1):
        if dado > 1:
            moveX = 1
            moveY = dado - 1
        else:
            moveX = 1
    elif(peca.casaX == 15 and peca.casaY == 8):
        if dado > 1:
            moveY = 1
            moveX = 1 - dado
        else:
            moveY = 1
    elif(peca.casaX == 8 and peca.casaY == 15):
        if dado > 1:
            moveX = -1
            moveY = 1 - dado
        else:
            moveX = -1
    elif(peca.casaX == 1 and peca.casaY == 8):
        if dado > 1:
            moveY = -1
            moveX = dado - 1
        else:
            moveY = -1
    elif(peca.casaX <= 7 and peca.casaX > 1 and peca.casaY == 8):
        if(peca.casaX + dado > 6):
            moveX = 7 - peca.casaX
        else:
            moveX = dado
    elif(peca.casaX >= 10 and peca.casaX < 15 and peca.casaY == 8):
        if(peca.casaX - dado < 10):
            moveX = 9 - peca.casaX
        else:
            moveX = -dado
    elif(peca.casaX == 8 and peca.casaY > 1 and peca.casaY <= 7):
        if(peca.casaY + dado > 6):
            moveY = 7 - peca.casaY
        else:
            moveY = dado
    elif(peca.casaX == 8 and peca.casaY >= 10 and peca.casaY < 15 ):
        if(peca.casaY - dado < 10):
            moveY = 9 - peca.casaY
        else:
            moveY = -dado
    return [moveX, moveY]
                    

def inicia():
    global lancaDado, salvar
    lancaDado.configure(state = NORMAL, background='LightBlue1', activebackground='LightBlue3')
    salvar.configure(state = NORMAL, background='LightBlue1', activebackground='LightBlue3')
    game_rules.novoJogo()
    updateJogador()
    desenha()
    
def lancamento():
    global dado, img, n
    updateJogador()
    n = game_rules.rolaDado()
    #dado.configure(text=str(n))
    print("n= ", n)
    foto = 'dado_' + str(n) + '.png'
    img = PhotoImage(file=foto)
    i = c.create_image(997.5,460,image=img)
#    desenha()
    
    

def updateJogador():
    global turno, cores
    cores = ['red4', 'dark green', 'goldenrod1', 'midnight blue']
    n = game_rules.vez
    turno.configure(text='A Jogar: ' + str(n))
    c.create_rectangle([980.5,443,1014.5, 477], outline=cores[(n-1)], width=5)
    
def drawBoard():
    global dado, turno, novoJogo, salvar, lancaDado
    for y in range(3):
        for x in range(6):
            if y == 1 and x != 0 or y == 0 and x == 1:
                color1 = 'red4'
                color2 = 'dark green'
            elif y == 2 and x == 1:
                color1 = 'gray4'
                color2 = 'gray4'
            else:
                color1 = 'gray97'
                color2 = 'gray97'
            c.create_rectangle(x*55+10, 340+55*y, x*55+10+55,(340+55*(y+1)),outline='gray4',width=2, fill=color1)
            c.create_rectangle(340+55*(2-y), x*55+10,(340+55*((2-y)+1),x*55+10+55),outline='gray4',width=2, fill=color2)

    for y in range(3):
        for x in range(6):
            if y == 1 and x != 5 or y == 2 and x == 4:
                color1 = 'goldenrod1'
                color2 = 'midnight blue'
            elif y == 0 and x == 4:
                color1 = 'gray4'
                color2 = 'gray4'
            else:
                color1 = 'gray97'
                color2 = 'gray97'
            c.create_rectangle(x*55+505, 340+55*y, x*55+55+505,(340+55*(y+1)),outline='gray4',width=2, fill=color1)
            c.create_rectangle(340+55*(2-y), x*55+505,(340+55*((2-y)+1),x*55+505+55),outline='gray4',width=2, fill=color2)

    c.create_polygon([80, 355, 105, 355+(380-355)/2, 80, 380],  fill='gray97')
    c.create_polygon([465, 80, 490, 80, 465+(490-465)/2, 105],  fill='gray97')
    c.create_polygon([765, 465, 740, 465+(490-465)/2, 765, 490],  fill='gray97')
    c.create_polygon([355, 765, 380, 765, 355+(380-355)/2, 740],  fill='gray97')


    rectanglered4 = c.create_rectangle(10,10,340,340,outline='gray4',width=2,fill='red4')
    rectangleBlue = c.create_rectangle(10,505,340,835,outline='gray4',width=2,fill='midnight blue')
    rectangledark_olive_green = c.create_rectangle(505,10,835,340,outline='gray4',width=2,fill='dark green')
    rectanglegoldenrod1 = c.create_rectangle(505,505,835,835,outline='gray4',width=2,fill='goldenrod1')

    pontos = [50, 210, 545, 705]
    for x in pontos:
        for y in pontos:
            c.create_oval(x,y,(x+70),(y+70), outline='gray4',width=2,fill='gray97')

    c.create_polygon([340, 340, 340+(505-340)/2, 340+(505-340)/2, 340, 505], outline='gray4', fill='red4', width=2)
    c.create_polygon([340, 340, 340+(505-340)/2, 340+(505-340)/2, 505, 340], outline='gray4', fill='dark green', width=2)
    c.create_polygon([505, 340, 340+(505-340)/2, 340+(505-340)/2, 505, 505], outline='gray4', fill='goldenrod1', width=2)
    c.create_polygon([340, 505, 340+(505-340)/2, 340+(505-340)/2, 505, 505], outline='gray4', fill='midnight blue', width=2)

    novoJogo = Button(text='Novo Jogo', height = 3, width = 20, command=inicia, background='LightBlue2', activebackground='LightBlue3')
    w = c.create_window(927.5,120, window=novoJogo,anchor=W)
    
    carregarJogo = Button(text='Carregar Jogo', height = 3, width = 20, background='LightBlue2', activebackground='LightBlue3')
    w = c.create_window(927.5,205, window=carregarJogo,anchor=W)
    
    salvar = Button(text='Salvar', height = 3, width = 20, background='gainsboro', state = DISABLED)
    w = c.create_window(927.5,290, window=salvar,anchor=W)
    
    turno = Label(text='A Jogar: ', height = 3, width = 20)
    w = c.create_window(927.5,375, window=turno,anchor=W)
    
    lancaDado = Button(text='Lançar Dado', height = 3, width = 20, command=lancamento, background='gainsboro', state = DISABLED)
    w = c.create_window(927.5,545, window=lancaDado,anchor=W)
    mainloop()

def desenha():
    global turno, cores, xis
    cores = ['red4', 'dark green', 'goldenrod1', 'midnight blue']
    n = game_rules.vez
    contador = 0
    tags = ["vermelho1", "vermelho2", "vermelho3", "vermelho4", "verde1", "verde2", "verde3", "verde4", "amarelo1", "amarelo2", "amarelo3", "amarelo4", "azul1", "azul2", "azul3", "azul4"]
#    for cor in game_rules.pecasDic.values():
#        x = cor.casaX
#        y = cor.casaY
#
#        c.create_oval(55*(x-1) + 15, 55*(y-1) + 15, 55*(x-1) + 60, 55*(y-1) + 60,outline='gray4',width=2,fill=cores[(n-1)])

    for cor in game_rules.pecasDic:
        for peca in cor:
            x = peca.posIni[0]
            y = peca.posIni[1]
            
            c.create_oval(55*(x-1) + 15, 55*(y-1) + 15, 55*(x-1) + 60, 55*(y-1) + 60,outline='gray4',width=2,fill=cores[xis], tag = tags[contador])
            contador += 1
        
        xis += 1
            

