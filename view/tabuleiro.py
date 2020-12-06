__all__ = ['c', 'updateJogador', 'Enable', 'lancaDado', 'Dado1', 'Dado2', 'Dado3', 'Dado4', 'Dado5', 'Dado6']

from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter.filedialog import asksaveasfile
from tkinter.filedialog import askdirectory
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

def Enable():
    global lancaDado, Dado1, Dado2, Dado3, Dado4, Dado5, Dado6, salvar
    updateJogador()
    lancaDado.configure(state = NORMAL,background='LightBlue1', activebackground='LightBlue3')
    Dado1.configure(state = NORMAL,background='LightBlue1', activebackground='LightBlue3')
    Dado2.configure(state = NORMAL,background='LightBlue1', activebackground='LightBlue3')
    Dado3.configure(state = NORMAL,background='LightBlue1', activebackground='LightBlue3')
    Dado4.configure(state = NORMAL,background='LightBlue1', activebackground='LightBlue3')
    Dado5.configure(state = NORMAL,background='LightBlue1', activebackground='LightBlue3')
    Dado6.configure(state = NORMAL,background='LightBlue1', activebackground='LightBlue3')
    salvar.configure(state = NORMAL,background='LightBlue1', activebackground='LightBlue3')

def CheckPeca(peca):
    global n
    if event_handler.pos != [None, None]:
        if peca.casaX == event_handler.pos[0] and peca.casaY == event_handler.pos[1]:
            if game_rules.CheckBarreiraSupremo(n) == False:
                if game_rules.CheckBarreira(peca, n) == False:
                    posicoes = MovePeca(peca,n)
                    c.move(peca.tag, (posicoes[0] - peca.casaX) * 55, (posicoes[1] - peca.casaY) * 55)
                    peca.casaX = posicoes[0]
                    peca.casaY = posicoes[1]
                    game_rules.lastMoved = peca
                    game_rules.Captura(peca)                   
                    if game_rules.CheckWin() == True:
                        game_rules.SomaPontos()
                        return
        
                    game_rules.check6(n)
            else:
                if game_rules.vez == 4:
                    game_rules.vez = 1
                else:
                    game_rules.vez += 1
            Enable()

def MovePeca(peca, dado):
    peca.casasAndadas += dado
    if peca.casasAndadas >= 58:
        peca.casasAndadas = 58

    if peca in game_rules.pecasDic[0]:
        return game_rules.caminhoVermelho[peca.casasAndadas]
    elif peca in game_rules.pecasDic[1]:
        return game_rules.caminhoVerde[peca.casasAndadas]
    elif peca in game_rules.pecasDic[2]:
        return game_rules.caminhoAmarelo[peca.casasAndadas]
    else:
        return game_rules.caminhoAzul[peca.casasAndadas]
    
                    

def inicia():
    print('alguma coisa\nalguma outra coisa\n')
    global lancaDado, salvar, Dado1, Dado2, Dado3, Dado4, Dado5, Dado6
    lancaDado.configure(state = NORMAL, background='LightBlue1', activebackground='LightBlue3')
    Dado1.configure(state = NORMAL, background='LightBlue1', activebackground='LightBlue3')
    Dado2.configure(state = NORMAL, background='LightBlue1', activebackground='LightBlue3')
    Dado3.configure(state = NORMAL, background='LightBlue1', activebackground='LightBlue3')
    Dado4.configure(state = NORMAL, background='LightBlue1', activebackground='LightBlue3')
    Dado5.configure(state = NORMAL, background='LightBlue1', activebackground='LightBlue3')
    Dado6.configure(state = NORMAL, background='LightBlue1', activebackground='LightBlue3')
    salvar.configure(state = NORMAL, background='LightBlue1', activebackground='LightBlue3')
    game_rules.novoJogo()
    updateJogador()
    desenha()

def Load():
    data = [("text files","*.txt"),("all files", "*.*")]
    input = filedialog.askopenfile(initialdir = ".", title = "Abrir arquivo", filetypes = data)
    print(input)
    game_rules.vez = int(input.readline())
    Enable()
    

def Save():
    data = [("text files","*.txt"),("all files", "*.*")]
    file = asksaveasfile(title = "Salvar como", initialdir = ".", filetypes = data, defaultextension = ".txt")
    #file.write(str(game_rules.pecasDic)+'\n')
    file.write(str(game_rules.vez))
    print(file)
    
def lancamento(valor):
    global dado, img, n, lancaDado, Dado1, Dado2, Dado3, Dado4, Dado5, Dado6
    if(valor == None):
        n = game_rules.rolaDado()
    else:
        n = valor
    foto = 'dado_' + str(n) + '.png'
    img = PhotoImage(file=foto)
    i = c.create_image(997.5,460,image=img)
    lancaDado.configure(state = DISABLED)
    Dado1.configure(state = DISABLED)
    Dado2.configure(state = DISABLED)
    Dado3.configure(state = DISABLED)
    Dado4.configure(state = DISABLED)
    Dado5.configure(state = DISABLED)
    Dado6.configure(state = DISABLED)
    salvar.configure(state = DISABLED)
    game_rules.check5(n)

    

def updateJogador():
    global turno, cores
    cores = ['red4', 'dark green', 'goldenrod1', 'midnight blue']
    n = game_rules.vez
    turno.configure(text='A Jogar: ' + str(n))
    c.create_rectangle([980.5,443,1014.5, 477], outline=cores[(n-1)], width=5)
    
def drawBoard():
    global dado, turno, novoJogo, salvar, lancaDado, Dado1, Dado2, Dado3, Dado4, Dado5, Dado6, salvar
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
    
    carregarJogo = Button(text='Carregar Jogo', height = 3, width = 20, command = Load, background='LightBlue2', activebackground='LightBlue3')
    w = c.create_window(927.5,205, window=carregarJogo,anchor=W)
    
    salvar = Button(text='Salvar', height = 3, width = 20, command = Save, background='gainsboro', state = DISABLED)
    w = c.create_window(927.5,290, window=salvar,anchor=W)
    
    turno = Label(text='A Jogar: ', height = 3, width = 20)
    w = c.create_window(927.5,375, window=turno,anchor=W)
    
    lancaDado = Button(text='Lançar Dado', height = 3, width = 20, command=lambda:lancamento(None), background='gainsboro', state = DISABLED)
    w = c.create_window(927.5,545, window=lancaDado,anchor=W)

    dados = Label(text='Escolha o dado: ', height = 3, width = 20)
    w = c.create_window(927.5,600, window=dados,anchor=W)

    Dado1 = Button(text='1', height = 3, width = 5, command=lambda:lancamento(1), background='gainsboro', state = DISABLED)
    w = c.create_window(927.5,645, window=Dado1,anchor=W)

    Dado2 = Button(text='2', height = 3, width = 5, command=lambda:lancamento(2), background='gainsboro', state = DISABLED)
    w = c.create_window(977.5,645, window=Dado2,anchor=W)

    Dado3 = Button(text='3', height = 3, width = 5, command=lambda:lancamento(3), background='gainsboro', state = DISABLED)
    w = c.create_window(1027.5,645, window=Dado3,anchor=W)

    Dado4 = Button(text='4', height = 3, width = 5, command=lambda:lancamento(4), background='gainsboro', state = DISABLED)
    w = c.create_window(927.5,710, window=Dado4,anchor=W)

    Dado5 = Button(text='5', height = 3, width = 5, command=lambda:lancamento(5), background='gainsboro', state = DISABLED)
    w = c.create_window(977.5,710, window=Dado5,anchor=W)

    Dado6 = Button(text='6', height = 3, width = 5, command=lambda:lancamento(6), background='gainsboro', state = DISABLED)
    w = c.create_window(1027.5,710, window=Dado6,anchor=W)
    
    mainloop()

def desenha():
    global turno, cores, xis
    cores = ['red4', 'dark green', 'goldenrod1', 'midnight blue']
    n = game_rules.vez
    contador = 0
    xis = 0
    tags = ["vermelho1", "vermelho2", "vermelho3", "vermelho4", "verde1", "verde2", "verde3", "verde4", "amarelo1", "amarelo2", "amarelo3", "amarelo4", "azul1", "azul2", "azul3", "azul4"]

    for cor in game_rules.pecasDic:
        for peca in cor:
            x = peca.casaX
            y = peca.casaY
            
            c.create_oval(55*(x-1) + 15, 55*(y-1) + 15, 55*(x-1) + 60, 55*(y-1) + 60,outline='gray4',width=2,fill=cores[xis], tag = tags[contador])
            contador += 1
        
        xis += 1
            

