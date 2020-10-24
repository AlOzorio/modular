from tkinter import *
root = Tk()
root.geometry('1170x845+410+130')
root.title('Ludo')
c = Canvas(root, width=1170, height=845)
c.pack()
bigRectangle = c.create_rectangle(10, 10, 835,835,outline='black',width=2)


def lancamento():
    n=int(dado.configure('text')[4])+1
    dado.configure(text=str(n))


for y in range(3):
    for x in range(6):
        if y == 1 and x != 0 or y == 0 and x == 1:
            color1 = 'red'
            color2 = 'green'
        elif y == 2 and x == 1:
            color1 = 'black'
            color2 = 'black'
        else:
            color1 = 'white'
            color2 = 'white'
        c.create_rectangle(x*55+10, 340+55*y, x*55+10+55,(340+55*(y+1)),outline='black',width=2, fill=color1)
        c.create_rectangle(340+55*(2-y), x*55+10,(340+55*((2-y)+1),x*55+10+55),outline='black',width=2, fill=color2)

for y in range(3):
    for x in range(6):
        if y == 1 and x != 5 or y == 2 and x == 4:
            color1 = 'yellow'
            color2 = 'blue'
        elif y == 0 and x == 4:
            color1 = 'black'
            color2 = 'black'
        else:
            color1 = 'white'
            color2 = 'white'
        c.create_rectangle(x*55+505, 340+55*y, x*55+55+505,(340+55*(y+1)),outline='black',width=2, fill=color1)
        c.create_rectangle(340+55*(2-y), x*55+505,(340+55*((2-y)+1),x*55+505+55),outline='black',width=2, fill=color2)

c.create_polygon([80, 355, 105, 355+(380-355)/2, 80, 380],  fill='white')
c.create_polygon([465, 80, 490, 80, 465+(490-465)/2, 105],  fill='white')
c.create_polygon([765, 465, 740, 465+(490-465)/2, 765, 490],  fill='white')
c.create_polygon([355, 765, 380, 765, 355+(380-355)/2, 740],  fill='white')


rectangleRed = c.create_rectangle(10,10,340,340,outline='black',width=2,fill='red')
rectangleBlue = c.create_rectangle(10,505,340,835,outline='black',width=2,fill='blue')
rectangleGreen = c.create_rectangle(505,10,835,340,outline='black',width=2,fill='green')
rectangleYellow = c.create_rectangle(505,505,835,835,outline='black',width=2,fill='yellow')

pontos = [50, 210, 545, 705]
for x in pontos:
    for y in pontos:
        c.create_oval(x,y,(x+70),(y+70), outline='black',width=2,fill='white')

c.create_polygon([340, 340, 340+(505-340)/2, 340+(505-340)/2, 340, 505], outline='black', fill='red', width=2)
c.create_polygon([340, 340, 340+(505-340)/2, 340+(505-340)/2, 505, 340], outline='black', fill='green', width=2)
c.create_polygon([505, 340, 340+(505-340)/2, 340+(505-340)/2, 505, 505], outline='black', fill='yellow', width=2)
c.create_polygon([340, 505, 340+(505-340)/2, 340+(505-340)/2, 505, 505], outline='black', fill='blue', width=2)

novoJogo = Button(text='Novo Jogo', height = 3, width = 20, background='SteelBlue1', activebackground='SteelBlue3')
w = c.create_window(927.5,120, window=novoJogo,anchor=W)
carregarJogo = Button(text='Carregar Jogo', height = 3, width = 20, background='SteelBlue1', activebackground='SteelBlue3')
w = c.create_window(927.5,205, window=carregarJogo,anchor=W)
salvar = Button(text='Salvar', height = 3, width = 20, background='CadetBlue1', activebackground='SteelBlue3')
w = c.create_window(927.5,290, window=salvar,anchor=W)
dado = Label(text='Á Jogar:', height = 3, width = 20)
w = c.create_window(927.5,375, window=dado,anchor=W)
dado = Label(text='0', height = 3, width = 20)
w = c.create_window(927.5,460, window=dado,anchor=W)
lancaDado = Button(text='Lançar Dado', height = 3, width = 20, command=lancamento, background='CadetBlue1', activebackground='SteelBlue3')
w = c.create_window(927.5,545, window=lancaDado,anchor=W)
mainloop()
