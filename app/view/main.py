# importa a janela base
from app.help.window import BaseWindow

# importa a View para inserir os dados no HTML
from app.help.View import View

#importa o tkinter e a ferramenta necessária para compor a janela com HMTL
from tkinter import *
from tkhtmlview import HTMLLabel


class MainWin:

    def showMainWindow(args):
        
        # coordenadas X e Y da janlea
        x = 800
        y = 800

        # instancia a View e da o mearge com os dados recebidos para criar os cards de tarefas
        render = View
        html = render.mearge('main', args)
        
        # cria uma nova instância de janela
        window = BaseWindow.start('main', f'{x}x{y}')

        # cria o botão de nova tarefa, e o fixa no topo à direita
        btn = Button(window, text='Novo', bg="green")
        btn.pack(anchor='ne')

        # cria os cards de tarefas
        r = 1
        html_label = ''
        arr = []
        for c in range(0, len(html)):
            body = Label(window)
            card = html[c]
            html_label = HTMLLabel(body, html=card, width=50, height=10)
            
            if(c == 0):
               
                html_label.grid(row=1, column=1)
            elif(c%3 != 0):
                
                html_label.grid(row=1, column=2)
            else:
                
                r = r+1
                
                html_label.place(x=c, y=r)

            arr.append(html_label)

            body.pack()
        # retorna o Botão para o controller
        return [btn, arr, window]