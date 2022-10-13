from re import L
from time import sleep
class View:

    def mearge(file, args):
        
        # abre o arquivo
        file = open(f'app/view/pages/{file}.html', 'r')

        # cria nossa array que se tornará uma string igual o arquivo, para pordermos editar
        arr = []

        # transforma nosso arquivo em uma array para podermos edita-lo
        for l in file:
            if (l != '\n'):
                arr.append(l)
        
        # fecha o arquivo aberto
        file.close()

        # transforma nossa array com as linhas do arquivo em uma string
        f = ''.join(arr)
        
        # uma lista que conterá o código html de todas as tarefas
        tasks = []
        
        # para cada tarefa que existe
        for task in args:
            code = []
            l = f
            # para cada chave dentro da task
            for key in task:
                if (key == 'color'):
                    color = task[key].replace('0x', '#')
                    # se a chave for color, substituí trocando 0x por #
                    l = l.replace(f'[[{key}]]', color)
                else:
                    # se existe um campo de substituição para esta chave, ele faz o replace
                    l = l.replace(f'[[{key}]]', str(task[key]))
                code.append(l)

            tasks.append(code[-1])
        return tasks