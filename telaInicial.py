from tkinter import *
root = Tk()
root.geometry('1170x845+410+130')
root.title('Ludo')
c = Canvas(root, width=1170, height=845)
c.pack()

    
# declaring string variable 
# for storing name and password 
nomeJogador=StringVar()
corEscolhida=Label(root, width = 27, height = 2, background='white') 
# defining a function that will 
# get the name and password and  
# print them on the screen 
def confirmar(): 
  
    name=nomeEntrada.get()
      
    print("Nome : " + name)
    print("Cor : " + corJogador)
      
    nomeJogador.set("")
    corEscolhida=Label(root, width = 27, height = 2, background='white')
    w = c.create_window(570.5,350, window=corEscolhida,anchor=W)

def azul():
    global corJogador
    corJogador = "azul"
    corEscolhida=Label(root, width = 27, height = 2, background='blue')
    w = c.create_window(570.5,350, window=corEscolhida,anchor=W)

def vermelho():
    global corJogador
    corJogador = "vermelho"
    corEscolhida=Label(root, width = 27, height = 2, background='red')
    w = c.create_window(570.5,350, window=corEscolhida,anchor=W)

def amarelo():
    global corJogador
    corJogador = "amarelo"
    corEscolhida=Label(root, width = 27, height = 2, background='yellow')
    w = c.create_window(570.5,350, window=corEscolhida,anchor=W)

def verde():
    global corJogador
    corJogador = "verde"
    corEscolhida=Label(root, width = 27, height = 2, background='green')
    w = c.create_window(570.5,350, window=corEscolhida,anchor=W)
      

# creating a label for  
# name using widget Label 
name_label = Label(root, text = 'Nome', 
                      font=('calibre', 
                            15, 'bold')) 
   
# creating a entry for input 
# name using widget Entry 
nomeEntrada = Entry(root, 
                      textvariable = nomeJogador,width = 17,font=('calibre',15, 'normal')) 
   
# creating a label for password 
cor_label = Label(root, 
                       text = 'Cor', 
                       font = ('calibre',15,'bold')) 
   
# creating a entry for password 
corAzul=Button(root, command = azul, width = 5, background='blue', activebackground='midnight blue') 
corVermelha=Button(root, command = vermelho, width = 5, background='red', activebackground='red4') 
corAmarela=Button(root, command = amarelo, width = 5, background='yellow' , activebackground='yellow4') 
corVerde=Button(root, command = verde, width = 5, background='green', activebackground='dark green') 

   
# creating a button using the widget  
# Button that will call the confirmar function  
sub_btn=Button(root,text = 'Confirmar', font = ('calibre',15,'normal'),
                  command = confirmar, width = 23, background='SteelBlue3', activebackground='CadetBlue1') 
   
# placing the label and entry in 
# the required position using grid 
# method

w = c.create_window(500.5,300, window=name_label,anchor=W)
w = c.create_window(570.5,300, window=nomeEntrada,anchor=W)
w = c.create_window(500.5,350, window=cor_label,anchor=W)
w = c.create_window(570.5,350, window=corEscolhida,anchor=W)
w = c.create_window(570.5,400, window=corAzul,anchor=W)
w = c.create_window(620.5,400, window=corVermelha,anchor=W)
w = c.create_window(670.5,400, window=corAmarela,anchor=W)
w = c.create_window(720.5,400, window=corVerde,anchor=W)
w = c.create_window(500.5,450, window=sub_btn,anchor=W)
   
# performing an infinite loop  
# for the window to display 
root.mainloop()
