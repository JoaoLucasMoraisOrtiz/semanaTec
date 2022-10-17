from app.view.create import CreateWin
from app.controller.Priority import Priority
from app.API.tasks import DbMethods
from tkinter import END, messagebox
import re
from json import load

# variáveis globais
cond = 1

f = open('secrets.json')
data = load(f)
table = data['taskTable']

class createController:

    def awaitReturn(task):
        global table

        calculator = Priority
        arr = calculator.priority(task)
        db = DbMethods
        db.dbActions(table, 'CREATE', arr)
        return True

    def dataMatch(data, mainWin):
        
        americanDate = r'[1-9][0-9][0-9][0-9][\s]?[/-][\s]?[0-9]?[0-9][\s]?[/-][\s]?[0-9]?[0-9]'
        brazilianDate = r'[0-9][0-9][\s]?[/-][\s]?[0-9]?[0-9][\s]?[/-][\s]?[1-9][0-9][0-9][0-9]'
        if (re.search(americanDate, data)):
            data = data.replace(' ', '')
            data = data.replace('/', '-')

            year = day = data[0:data.index('-')]

            find = ''.join(re.findall('-[0-9]?[0-9]-', data))
            month = find.replace('-', '')

            day = data[-2:]

            fdata = f'{year}-{month}-{day}'
            print(fdata)

            if(int(year)==0 or int(month)==0 or int(day)==0):
                messagebox.showerror(
                'Erro de Data', 'o dia, mês ou ano é inválido')
                mainWin.iconify()
                return False
            else:
                if(int(day) > 31 or int(month) > 12):
                    messagebox.showerror(
                'Erro de Data', 'o dia ou o mês é inválido')
                    mainWin.iconify()
                    return False
                return [fdata, True]

        elif (re.search(brazilianDate, data)):

            data = data.replace(' ', '')
            data = data.replace('/', '-')
            year = data[-4:]

            # tratando do mês agora
            find = ''.join(re.findall('-[0-9]?[0-9]-', data))
            month = find.replace('-', '')

            day = data[0:data.index('-')]
            fdata = f'{year}-{month}-{day}'

            if(int(year) == 0 or int(month) == 0 or int(day) == 0):
                messagebox.showerror(
                'Erro de Data', 'o dia, mês ou ano é inválido')
                mainWin.iconify()
                return False
            else:
                if(int(day) > 31 or int(month) > 12):
                    messagebox.showerror(
                'Erro de Data', 'o dia ou o mês é inválido')
                    mainWin.iconify()
                    return False
                return [fdata, True]

        else:
            messagebox.showerror(
                'Erro de Data', 'sua entrada de data está errada, utilize apenas - (traço) ou / (barra) para separar dia, mês e ano.')
            mainWin.iconify()
            return False

    def isempty(task, mainWin):
        control = 0
        for elem in task:
            if elem != 'timeToDo':
                if task[elem] == '':
                    control = 1
                    messagebox.showerror(
                        'Oops', f'O unico campo opcional é o ultimo. Preencha todos os outros!')
                    mainWin.iconify()
                    break
        return control

    def turnOff():
        global cond
        cond += 1

    def newTask(obj, window, mainWin):
        """ obj = {
            "name": inputName,
            "date": inputDate,
            "timeToDo": inputTimeToDo,
            "timeToConc": inputTime,
            "porc": slidePorc,
            "selfPri": slidePri
        } """

        # window.wm_state('iconic')

        name = obj['name'].get('1.0', END).replace('\n', '')
        date = obj['date'].get('1.0', END).replace('\n', '')
        timeToDo = obj['timeToDo'].get('1.0', END).replace('\n', '')
        h = obj['timeToConc'].hours()
        m = obj['timeToConc'].minutes()
        timeToConc = f'{h}:{m}'
        prog = obj['porc'].get()
        selfPri = obj['selfPri'].get()

        task = {
            "name": name,
            "date": date,
            "timeToDo": timeToDo,
            "timeToConc": timeToConc,
            "prog": prog,
            "selfPri": selfPri/100
        }

        r = createController.isempty(task, mainWin)
        if (r == 0):
            task['date'] = task['date'].strip()
            date = createController.dataMatch(task['date'], mainWin)
            
            if(date[1] == True):

                task['date'] = date[0]
                task['color'] = '0xffffff'
                task['priority'] = 0

                count = 0
                a = False
                while True:
                    if(count == 0):
                        a = createController.awaitReturn(task)
                    else:
                        pass
                    if (a):
                        break
                
                window.destroy()
                global cond
                cond = 0
            else:
                pass
        else:
            pass

    def getCreate(mainWin):

        global cond
        cond = 1
        # mainWin.wm_state('iconic')
        # instancia a createWindow
        window = CreateWin

        ret = window.showCreateWindow()
        ret['btn'].config(command=lambda: createController.newTask(
            ret['obj'], ret['window'], mainWin))

        while cond:

            # define que fechar a janela termina o processo de execução
            ret['window'].protocol(
                "WM_DELETE_WINDOW", createController.turnOff())

            ret['window'].update_idletasks()

            ret['window'].update()
