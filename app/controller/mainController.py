from app.view.main import MainWin
from app.controller.createController import createController
from app.API.tasks import DbMethods
from tkinter import messagebox
from json import load

cond = 1

class mainController:

    def create(window):

        create = createController
        create.getCreate(window)
        messagebox.showinfo(
                    'Recarregar', f'A janela ira recarregar!')
        window.destroy()
        mainController.getMain()


    def delete(e, n):
        
        for element in n:
            if(element[1] == e):
                element[0].destroy()
                

    def turnOff():
        global cond
        cond += 1

    def getMain():

        # instancia a mainWindow
        window = MainWin

        # instancia DbMethods
        db = DbMethods

        # pega o json com os secrets
        f = open('secrets.json')
        data = load(f)

        # get dos dados do banco de dados
        tasks = db.dbActions(data['taskTable'], 'GET')

        # ordena por prioridade
        tasks = sorted(tasks, key=lambda d: d[-1], reverse=True)

        # lista que guardará os elementos de cada entrada
        args = []

        # para cada elemento vindo do banco de dados
        for element in tasks:
            # id, nome, dataEntrega, tempoConc, horarioConc, prog, selfPri, color, Priority
            args.append({"name": element[1],
                        "date": element[2],
                         "time": element[4],
                         "prog": element[5],
                         "color": element[7]})
        
        global elem
        # Gera as variáveis
        elem = window.showMainWindow(args)

        n = [0, 1, 2] 
        b=0
        command = ''
        for count in range(0, len(elem[1])):
            command = f"""elem[1][{count}][0].bind('<Button-1>', lambda e: mainController.delete({count}, elem[1]))"""
            exec(command)        

        
        parent = elem[2]._nametowidget(elem[2].winfo_parent())
        grand_parent = parent._nametowidget(parent.winfo_parent())
        instance = parent._nametowidget(grand_parent.winfo_parent())

        elem[0].configure(command=lambda: mainController.create(instance))

        
        global cond
        # cria o loop que mantem a janela na tela
        while cond:

            # define que fechar a janela termina o processo de execução
            instance.protocol("WM_DELETE_WINDOW", mainController.turnOff())
            
            for c in range(0, len(elem[1]), 1):
                try:
                    if (elem[1][c][0].winfo_exists()):
                        pass
                    else:
                        # deleta do banco de dados a tarefa
                        print(elem[1][c], ' FOI DE BASE')
                        print(tasks[elem[1][c][1]])
                        data = {"id": tasks[elem[1][c][1]][0]}
                        print(data)
                        db.dbActions('tasks', 'DELETE', data)
                        messagebox.showinfo(
                                    'Recarregar', f'A janela ira recarregar!')
                        instance.destroy()
                        mainController.getMain()
                        
                except:
                    pass

            elem[2].update_idletasks()

            elem[2].update()
