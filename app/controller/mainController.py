from app.view.main import MainWin
from app.API.tasks import DbMethods
from json import load


class mainController:

    def create():
        print('the skys are blue')

    def delete(elem):
        print(elem)

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

        # Gera as variáveis
        elem = window.showMainWindow(args)

        """ def tobind(e):
            e.bind('<Button-1>', lambda a: print('sad')) """

        for c in range(len(elem[1])-1, -1, -1):
           print(c)
           elem[1][c].bind('<Button-1>', lambda a: elem[1][c].destroy())
        

        elem[0].configure(command= lambda : mainController.create())

        #cria o loop que mantem a janela na tela
        while True:
            
            for c in range(0, len(elem[1]), 1):
                try:
                    if(elem[1][c].winfo_exists()):
                        pass
                    else:
                        # deleta do banco de dados a tarefa
                        print(elem[1][c], ' FOI DE BASE')
                        elem[1].pop(c)
                except:
                    pass

                
            elem[2].update_idletasks()

            elem[2].update()
