from textwrap import fill
from tkinter import *
from tkinter import ttk
# classe que cria nossa janela base
class BaseWindow:

    def preparation(name, size):
        #instancia o tikinter
        start_menu = Tk()

        #seta o parâmetro name como o nome da janela
        start_menu.title(name)

        #seta o parâmetro size como as dimenções da janela (no padrão: (X)x(Y), EX: 400x600)
        start_menu.geometry(size)
        return start_menu

    # método responsável por criar nossa instância de janela
    def start(name, size):

        window = BaseWindow.preparation(name, size)

        # cria um frame principal
        main_frame = Frame(window)
        main_frame.pack(fill=BOTH, expand=1)

        # cria um Canvas
        my_canvas = Canvas(main_frame)
        my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

        # cria uma scrollbar no canvas
        my_scroll = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
        my_scroll.pack(side=RIGHT, fill=Y)

        # configura a ação de scroll da scrollbar
        my_canvas.configure(yscrollcommand=my_scroll.set)
        my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox('all'))) 

        #secound frame recebe o canvas
        second_frame = Frame(my_canvas)
        
        #adciona o second_frame quando a janela é criada, fazendo-o ocupar toda a janela no width
        my_canvas.create_window((0,0), window=second_frame, anchor='nw', width=int(size[0:int(size.find('x'))])-10)

        
        #retorna o second_frame, que é onde devemos inserir os objetos de nossa janela
        return second_frame