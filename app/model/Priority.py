# importa a classe datetime para trabalharmos com datas
import datetime
from math import ceil

'''
    color = int('ffff00', 16)
    color -= 24400
    p = hex(color)
    print(f'tentando formatar color 10 para 16. ffff00 =? {p}')
    exit()
'''


class Priority:

    def setColor(p):
        if (0.9 < p):
            color = '0xf00000'
            p = color

        elif (0.8 < p < 0.9):
            color = '0xf06200'
            p = color

        elif (0.7 < p < 0.8):
            color = '0xf08600'
            p = color

        elif (0.6 < p < 0.7):
            color = '0xf0a800'
            p = color

        elif (0.5 < p < 0.6):
            color = '0xffc500'
            p = color

        elif (0.4 < p < 0.5):
            color = '0xffde00'
            p = color

        elif (0.3 < p < 0.4):
            color = '0xfff300'
            p = color

        elif (0.2 < p < 0.3):
            color = '0xffff00'
            p = color

        else:
            color = 0xffff8d
            p = color

        return p

    def userPriority(p):
        
        if (0.9 < p):
            p += 0.5

        elif (0.8 < p < 0.9):
            p += 0.45

        elif (0.7 < p < 0.8):
            p += 0.4

        elif (0.6 < p < 0.7):
            color = 0xf0a800
            p = color

        elif (0.5 < p < 0.6):
            p += 0.35

        elif (0.4 < p < 0.5):
            p += 0.3

        elif (0.3 < p < 0.4):
            p += 0.25

        elif (0.2 < p < 0.3):
            p += 0.2

        else:
            p += 0.15

        return p

    def priority(arr):

        # nossa prioridade
        p = float(arr["priority"])

        # recebe a data em dias de nossa tarefa
        d = datetime.datetime.strptime(arr["data"], "%Y-%m-%d")

        # caso a tarefa seja hoje
        if (datetime.date.today() == d):
            h = arr["timeToConc"].datetime.strftime('%H:%M')
            if (h < datetime.datetime.strftime('12:00')):
                p += 0.4
            else:
                p += 0.45

        # caso a tarefa não seja hoje
        else:
            
            # se o compromisso está à uma semana ou menos, acresce 0.3 em sua prioridade
            if (datetime.datetime.today() + datetime.timedelta(days=7) <= d):
                p += 0.3

            # se está à quinze dias, acrescenta 0.1 em sua prioridade
            elif (datetime.datetime.today() + datetime.timedelta(days=15) < d):
                p += 0.1

            # se está à mais de quinze dias, não adciona nada a sua prioridade
            elif (datetime.datetime.today() + datetime.timedelta(days=15) > d):
                p += 0

            # caso esteja entre uma semana e 15 dias, adciona 0.2 em sua prioridade
            else:
                p += 2

        # calcula a prioridade setada pelo usuário
        p = Priority.userPriority(p)
        
        # calcula a cor
        arr['color'] = Priority.setColor(p)
        arr["priority"] = p
        return arr

    