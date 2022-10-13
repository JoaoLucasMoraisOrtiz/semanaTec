# importa a classe priority
from app.model.Priority import Priority

#importa as ações do banco de dados
from app.API.tasks import DbMethods

# array de exemplo
arr = {
    "name": "Fazer o TCC",
    "date": "2022-10-16",
    "timeToDo": 3,
    "timeToConc": "07:10",
    "prog": "70",
    "selfPri": 1,
    "color": '0xffffff',
    "priority": 0
}

# instancia priority
obj = Priority

dbMethods = DbMethods

# executa o método priority
newArr = obj.priority(arr)
print(newArr)

# salva a tarefa na DB
#dbMethods.dbActions('tasks', 'CREATE', arr)

# pega os dados da DB
#querry = dbMethods.dbActions('tasks', 'GET')
#print(querry)

# edita os dados da DB
#dbMethods.dbActions(table='tasks', action='UPDATE', data={"selfPri":0.8, "name":" Fazer o TCC "})

# deleta os dados da DB
#dbMethods.dbActions('tasks', 'DELETE', {"name":" Fazer o TCC "})