# importa a janela base
from app.help.window import BaseWindow

# importa a View para inserir os dados no HTML
from app.help.View import View

#importa o tkinter e a ferramenta necessária para compor a janela com HMTL
from tkinter import *
import tkinter as tkinter
from tkhtmlview import HTMLLabel


class MainWin:

    def showMainWindow(args):
        
        # coordenadas X e Y da janlea
        x = 1200
        y = 1200

        # instancia a View e da o mearge com os dados recebidos para criar os cards de tarefas
        render = View
        html = render.mearge('main', args)
        
        # cria uma nova instância de janela
        window = BaseWindow.start('main', f'{x}x{y}')

        # cria o botão de nova tarefa, e o fixa no topo à direita
        btn = Button(window, text='Novo', bg="green", height=2)
        btn.pack(anchor=tkinter.NE)

        # cria os cards de tarefas
        html_label = ''
        arr = []
        bdel = []

        """ posit = []
        x = 0
        for item in html:
            posit.append(x)
            x += 1 """

        for c in range(0, len(html)):
            #body = Label(window)
            card = html[c]
            html_label = HTMLLabel(window, html=card, width=50, height=10)

            if(c == 0):
                
                html_label.pack(side=tkinter.TOP)
            elif(c%3 != 0):

                if((c+1)%3 == 0):
                    html_label.pack(side=tkinter.TOP)
                else:
                    html_label.pack(side=tkinter.TOP)

            elif(c%3 == 0 ):
                html_label.pack(side=tkinter.TOP)

            #body.pack()
            arr.append([html_label, c])  
        
        # retorna o Botão para o controller
        return [btn, arr, window]