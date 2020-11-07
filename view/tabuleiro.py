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

def CheckPeca():
    global n
    if(event_handler.pos == [None, None]):
        print(False)
    else:
        for peca in game_rules.pecasDic[game_rules.vez - 1]:
            if peca.casaX == event_handler.pos[0] and peca.casaY == event_handler.pos[1]:
                posicoes = MovePeca(peca.casaX,peca.casaY,n)
                c.move(peca.tag, posicoes[0] * 55, posicoes[1] * 55)
                peca.casaX += posicoes[0]
                peca.casaY += posicoes[1]
        print(True)

def MovePeca(posX, posY, dado):
    moveX = 0
    moveY = 0
    if(posX <= 6 and posY == 7):
        moveX = dado
        if(posX + dado > 6):
            moveX = 6 - posX + 1
            moveY = 6 - posX - dado
    elif(posX == 9 and posY <= 6):
        moveY = dado
        if(posY + dado > 6):
            moveY = 6 - posY + 1
            moveX = posY + dado - 6
    elif(posX >= 10 and posY == 9):
        moveX = -dado
        if(posX - dado < 10):
            moveX = 10 - posX - 1
            moveY = dado + moveX + 1
    elif(posX == 7 and posY >= 10):
        moveY = -dado
        if(posY - dado < 10):
            moveX = - 10 + posY - dado 
            moveY = - posY + 10 - 1
    elif(posX == 7 and posY <= 6):
        moveY = -dado
        if(posY - dado < 1):
            moveY = -posY + 1
            moveX = dado + moveY
            if(moveX > 2):
                moveY += moveX - 2
                moveX = 2
    elif(posX >= 10 and posY == 7):
        moveX = dado
        if(posX + dado > 15):
            moveX = 6 - (posX - 9)
            moveY = dado - moveX
            if(moveY > 2):
                moveX -= moveY - 2
                moveY = 2
    elif(posX == 9 and posY >= 10):
        moveY = dado
        if(posY + dado > 15):
            moveY = 6 - (posY - 9)
            moveX = -(dado - moveY)
            if(moveX < -2):
                moveY += moveX + 2
                moveX = -2
    elif(posX <= 6 and posY == 9):
        moveX = -dado
        if(posX - dado < 1):
            moveX = -posX + 1
            moveY = - dado - moveX
            if(moveY < -2):
                moveX -= moveY + 2
                moveY = -2
    elif(posX == 8 and posY == 1):
        if dado > 1:
            moveX = 1
            moveY = dado - 1
        else:
            moveX = 1
    elif(posX == 15 and posY == 8):
        if dado > 1:
            moveY = 1
            moveX = 1 - dado
        else:
            moveY = 1
    elif(posX == 8 and posY == 15):
        if dado > 1:
            moveX = -1
            moveY = 1 - dado
        else:
            moveX = -1
    elif(posX == 1 and posY == 8):
        if dado > 1:
            moveY = -1
            moveX = dado - 1
        else:
            moveY = -1
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
    n = game_rules.rolaDado()
    #dado.configure(text=str(n))
    print("n= ", n)
    foto = 'dado_' + str(n) + '.png'
    img = PhotoImage(file=foto)
    i = c.create_image(997.5,460,image=img)
#    desenha()
    
    updateJogador()

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
    tags = ["vermelho1", "vermelho2", "verde", "amarelo", "azul"]
#    for cor in game_rules.pecasDic.values():
#        x = cor.casaX
#        y = cor.casaY
#
#        c.create_oval(55*(x-1) + 15, 55*(y-1) + 15, 55*(x-1) + 60, 55*(y-1) + 60,outline='gray4',width=2,fill=cores[(n-1)])

    for cor in game_rules.pecasDic:
        for peca in cor:
            x = peca.casaX
            y = peca.casaY
            
            c.create_oval(55*(x-1) + 15, 55*(y-1) + 15, 55*(x-1) + 60, 55*(y-1) + 60,outline='gray4',width=2,fill=cores[xis], tag = tags[contador])
            contador += 1
        
        xis += 1
            

