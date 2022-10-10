# importa a classe datetime para trabalharmos com datas
import datetime
from math import ceil


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
            p += 0.45

        elif (0.8 < p < 0.9):
            p += 0.4

        elif (0.7 < p < 0.8):
            p += 0.35

        elif (0.6 < p < 0.7):
            p += 0.3

        elif (0.5 < p < 0.6):
            p += 0.25

        elif (0.4 < p < 0.5):
            p += 0.2

        elif (0.3 < p < 0.4):
            p += 0.20

        elif (0.2 < p < 0.3):
            p += 0.15

        else:
            p += 0.1

        return p

    def progPriority(p):
        a = 0
        if (0 < p < 10):
            a += 0.50

        elif (10 < p < 20):
            a += 0.45

        elif (20 < p < 30):
            a += 0.4

        elif (30 < p < 40):
            a += 0.35

        elif (40 < p < 50):
            a += 0.3

        elif (60 < p < 70):
            a += 0.25

        elif (70 < p < 80):
            a += 0.2

        elif (80 < p < 90):
            a += 0.25

        else:
            a += 0.1

        return a

    def datePriority(d, arr):
        a = 0

        # caso a tarefa seja hoje
        if (datetime.date.today() == d):
            h = datetime.datetime.strptime(arr["timeToConc"], '%H:%M').time()
            # verifica se a tarefa é antes ou depois do meio dia
            if (h < datetime.datetime.strptime('12:00', '%H:%M').time()):
                # caso seja antes do meio dia
                a += 0.4
            else:
                # caso seja após o meio dia
                a += 0.35

        # caso a tarefa não seja hoje
        else:
            # se o compromisso está à uma semana ou menos
            if (datetime.datetime.today().date() + datetime.timedelta(days=7) >= d):  # type: ignore

                # percorre por 7 dias para saber quantos dias faltam para o acontecimento
                for c in range(1, 7, 1):

                    # encontra quanto tempo falta para o acontecimento, o tempo em dias é c
                    if (datetime.date.today() + datetime.timedelta(days=c) == d):

                        # se o tempo que demora para realizar a tarefa não estivar vazio
                        if (arr['timeToDo'] != ''):

                            # caso a distância de hoje até a data de entrega seja menor ou igual ao tempo de realização
                            if (datetime.timedelta(arr['timeToDo']) + datetime.date.today() >= d):
                                a += 1
                                break
                            else:
                                #se não, calcula normalmente
                                a += 0.29/(c**(29/100))
                                break
                        else:
                            #se o tempo estiver vasio, calcula apenas como prioridade normal
                            a += 0.29/(c**(29/100))
                            break

            # se está à quinze dias, calcula o acrescimo em sua prioridade
            elif (datetime.date.today() + datetime.timedelta(days=15) == d):
                a += 0.29/(15**(29/100))

            # se está à mais de quinze dias, não adciona nada a sua prioridade
            elif (datetime.date.today() + datetime.timedelta(days=15) < d):
                a += 0

            # caso esteja entre uma semana e 15 dias, adciona 0.2 em sua prioridade
            else:
                a += 0.19
        
        return a

    def priority(arr):

        # nossa prioridade
        p = float(arr["priority"])

        # recebe a data em dias de nossa tarefa
        d = datetime.datetime.strptime(arr["date"], "%Y-%m-%d").date()

        if (p < 1):
            p += Priority.datePriority(d, arr)

        if (p < 1):
            # calcula a prioridade setada pelo usuário
            p += Priority.userPriority(p)

        if (p < 1):
            # calcula a prioridade quanto ao progreço do projeto
            p += Priority.progPriority(p)

        # calcula a cor
        arr['color'] = Priority.setColor(p)

        if (p > 1):
            arr["priority"] = 1
        else:
            arr['priority'] = round(p, 2)
            
        return arr
