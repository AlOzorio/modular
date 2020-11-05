from tkinter import *
root = Tk()
root.geometry('512x512')
c = Canvas(root, width=512, height=512)
c.pack()
o = c.create_oval(1,1,200,100,outline='blue',width=5,fill='red')
widget = Button(text='Tk Canvas')
w = c.create_window(10,120,window=widget,anchor=W)
l = c.create_line(100,0,120,30,50,60,100,120,fill='black',width=2)
r = c.create_rectangle(40,150,100,200,fill='white')

img = PhotoImage(file='dado_4.png')
i = c.create_image(100,100,image=img,anchor=NW)

a = c.create_arc (100,90,150,190,start=30,extent=60,\
outline='green',fill='orange')
t = c.create_text(200,35,text='Texto\nTexto',font='Arial 22')
mainloop()
