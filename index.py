# importa a classe priority
from app.model.Priority import Priority

# array de exemplo
arr = {
    "task": "Fazer o TCC",
    "data": "2022-11-09",
    "timeToDo": "",
    "timeToConc": "07:10",
    "prog": "70",
    "selfPri": 1,
    "color": 0xffffff,
    "priority": 0
}

# instancia priority
obj = Priority

# executa o método priority
newArr = obj.priority(arr)
print(newArr)
