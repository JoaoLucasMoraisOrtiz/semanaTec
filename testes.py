from cgitb import text
from os import kill
from tkinter import *
from tokenize import String
from tracemalloc import start

from setuptools import Command

def teste():
    print('helloo!!')

def funcArg(message):
    print(message)

def funcArg2(message):
    label7['text'] = message

def sumOne(var):
    var.set(int(var.get()) + 1)

#instancia o tikinter
start_menu = Tk()

#aciona o evento title
start_menu.title('teste1')

#determina a largura da janela
start_menu.geometry("500x600")

""" #determina que a janela não pode ser redimensionada em X e Y
start_menu.resizable(False,False) """

#cria um botão cujo pai é o start_menu, com o texto text e quando clickado, executa a func teste
btn = Button(start_menu, text = "teste", command=teste)

#adiciona efetivamente o botão (repare que o pack é que define que o elemento está sendo inciado)
btn.pack()

#para passarmos uma função com argumento, devemos adicionar a função com o "lamdbda:" antes
btn2 = Button(start_menu, text="func com argumento", command=lambda: funcArg('world!'))
btn2.pack()

#cria um label, o parâmetro bg altera a cor do background e font muda a fonte e outras coisas
label = Label(start_menu, text="olá mundo!!", bg="#ff88aa", font="Times 14 italic bold")
label.pack()

#a propriedade fg altera a cor do text
label2 = Label( start_menu, 
                text="hell o world!!", 
                bg="#ffffaa", 
                font="Times 14 italic bold", 
                fg='#00aaee')
label2.pack()

#a janela faz um wrap do tamanho da label
label3 = Label( start_menu, 
                width=2,
                text="blabla\nblablabla",
                height=2,
                bg="#ff0000")
label3.pack()

#borda na label
label4 = Label( start_menu, 
                text='soolid',
                bd=2,
                #determina o tipo de borda
                relief="solid",
                bg="#ffff00").pack()

#alinhamento do texto
label5 = Label( start_menu, 
                text='soolid',
                width=20,
                height=4,
                #o alinhamento é determinado pelos pontos cardeais N, S, L, W...
                anchor=NW,
                bg="#ffff00").pack()

label6 = Label( start_menu,
                text = 'teste de padding\nteeeste de padding',
                bd = 2,
                relief='solid',
                padx= 20,
                pady = 10,
                #podemos, caso precisarmos, justificar o texto, entretanto ele não juntará o texto à borda, 
                #isto é o anchor que faz
                justify=RIGHT).pack()


#cria uma label vazia
label7 = Label(start_menu)
#adiciona-a
label7.pack()

#adiciona um texto a ela
label7.configure(text='oláá')

#troca seu texto
btn3 = Button(start_menu, text='adicionar outro texto acima', command=lambda: funcArg2('oi')).pack()

#cria uma variável de texto (tkinter obj)
varText = StringVar()
varText.set('1')

#cria uma label que sempre terá o valor de text
label8 = Label( start_menu,
                textvariable=varText)
label8.pack()

#adicionamos um botão que muda o texto do varText
btn4 = Button(  start_menu,
                text='somar +1',
                command = lambda: sumOne(varText)).pack()

#determina que deve executar sempre a aplicação
start_menu.mainloop()