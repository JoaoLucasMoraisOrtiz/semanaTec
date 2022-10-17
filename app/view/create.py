# importa a janela base
from app.help.window import BaseWindow

from tktimepicker import AnalogPicker, AnalogThemes

# importa o tkinter e a ferramenta necessária para compor a janela com HMTL
from tkinter import *
import tkinter as tkinter

import asyncio

arr = 0

class CreateWin:

    def getData(obj):

        global arr

        minutes = obj['timeToConc'].minutes()
        hour = obj['timeToConc'].hours()

        name = obj['name'].get('1.0', END)
        date = obj['date'].get('1.0', END)
        timeToDo = obj['timeToDo'].get('1.0', END)
        timeToConc = f'{hour}:{minutes}:'
        porc = obj['Porc'].get()
        selfPri = obj['SelfPri'].get()

        arr = {
            "name": name,
            "date": date,
            "timeToDo": timeToDo,
            "timeToConc": timeToConc,
            "prog": porc,
            "selfPri": selfPri,
            "color": '',
            'priority':0,
            "save": obj['save'],
            "instance": obj['instance']
        }
        return arr

    def showCreateWindow():

        # coordenadas X e Y da janlea
        x = 450
        y = 600

        instance = BaseWindow.preparation('criar Tarefa', f'{x}x{y}')
        
        instance.lift()
        # cria uma nova instância de janela
        window = BaseWindow.start(
            'criar Tarefa', f'{x}x{y}', instance=instance)

        # label de texto 1
        lb1 = tkinter.Label(window, text='Qual o nome da tarefa?')
        lb1.pack(pady=5)

        # cria uma caida de texto:
        inputName = tkinter.Text(window,
                                 height=1,
                                 width=40)
        inputName.pack(pady=5)

        # label de texto 2
        lb2 = tkinter.Label(
            window, text='Qual a data que ela dever ser concluída?')
        lb2.pack(pady=5)

        # cria outra caida de texto:
        inputDate = tkinter.Text(window,
                                 height=1,
                                 width=40)
        inputDate.pack(pady=5)

        # label de texto 3
        lb3 = tkinter.Label(
            window, text='Qual o horário que você deve concluír a tarefa?')
        lb3.pack(pady=5)

        # cria o relógio:
        inputTime = AnalogPicker(window)
        inputTime.pack(fill=tkinter.BOTH)

        theme = AnalogThemes(inputTime)
        theme.setDracula()

        # label de texto 4
        lb4 = tkinter.Label(
            window, text='Quantos por cento da sua tarefa está concluída?')
        lb4.pack(pady=5)

        # cria um slide para a porcentágem:
        slidePorc = Scale(window, from_=0, to=100,
                          tickinterval=10, orient=HORIZONTAL, length=400)
        slidePorc.pack(pady=5)

        # label de texto 5
        lb5 = tkinter.Label(
            window, text='De 0 à 100, qual o nível de prioridade desta tarefa?')
        lb5.pack(pady=5)

        # cria um slide para a porcentágem:
        slidePri = Scale(window, from_=0, to=100,
                         tickinterval=10, orient=HORIZONTAL, length=400)
        slidePri.pack(pady=5)

        # label de texto 6
        lb2 = tkinter.Label(
            window, text='Quanto tempo em dias você levará para realizar esta tarefa?')
        lb2.pack(pady=5)

        # cria outra caida de texto:
        inputTimeToDo = tkinter.Text(window,
                                     height=1,
                                     width=40)
        inputTimeToDo.pack()

        # cria o botão de criar tarefa, e o fixa no topo à direita
        btn = Button(window, text='Criar', bg="green", height=1)
        btn.pack(side=tkinter.BOTTOM, anchor='s')

        obj = {
            "name": inputName,
            "date": inputDate,
            "timeToDo": inputTimeToDo,
            "timeToConc": inputTime,
            "porc": slidePorc,
            "selfPri": slidePri
        }
        
        # retorna o Botão para o controller
        return {"btn":btn, "obj":obj, "window":instance}
