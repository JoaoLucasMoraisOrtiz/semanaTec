from app.help.connection import Connection


class DbMethods:
    
    def dbActions(table, action, data=''):
        conn = Connection.conn()
        cursor = conn.cursor()

        #função de create
        if (action.upper() == 'CREATE'):
            try:
                insert = f"INSERT INTO {table} VALUES ({0}, \" {data['name']} \", \"{data['date']}\", \"{data['timeToDo']}\", \"{data['timeToConc']}\", {data['prog']}, {data['selfPri']}, \"{data['color']}\", \"{data['priority']}\")"
                print(insert)
                
                cursor.execute(insert)
                conn.commit()
                cursor.close()
            except ValueError:
                cursor.close()
                return 'Tivemos um erro ao gravar sua tarefa no Banco de Dados'
        
        #função de read
        elif (action.upper() == 'GET'):
            if(data == ''):
                try:
                    querry = f'SELECT * FROM {table}'
                    cursor.execute(querry)
                    querry = cursor.fetchall()
                    cursor.close()
                    return querry
                except ValueError:
                    return 'Tivemos um erro ao acessar suas tarefas no Banco de Dados'
            else:
                try:

                    for key in data:
                        querry = f'SELECT * FROM {table} WHERE {key} = {data[key]}'
                    
                    cursor.execute(querry)
                    querry =  cursor.fetchall()
                    cursor.close()
                    return querry
                except ValueError:
                    cursor.close()
                    return 'Tivemos um erro ao acessar suas tarefas no Banco de Dados'
        
        #função de update
        elif (action.upper() == 'UPDATE'):
            try:

                update = f'UPDATE {table} set {list(data.keys())[0]}=\"{data[list(data.keys())[0]]}\" WHERE {list(data.keys())[1]}=\"{data[list(data.keys())[1]]}\";'
                cursor.execute(update)
                conn.commit()
                cursor.close()
            except ValueError:
                cursor.close()
                return 'Tivemos um erro ao gravar suas alterações no Banco de dados'

        #function delete
        elif (action.upper() == 'DELETE'):
            try:
                delete = f'DELETE FROM {table} WHERE {list(data.keys())[0]}=\"{data[list(data.keys())[0]]}\";'
                print(delete)
                cursor.execute(delete)
                conn.commit()
            except ValueError:
                return 'Tivemos um erro ao gravar suas alterações no Banco de dados'
