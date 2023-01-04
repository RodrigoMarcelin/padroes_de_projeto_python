import sqlite3

def _executar(query):
    db_path = r"C:\Users\RodrigoAmorim\Documents\Rodrigo\padroes_de_projeto_python\Padrões de Projeto compostos\MVC\geek.university"
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    resultado = None


    try:
        cursor.execute(query)
        resultado = cursor.fetchall()
        connection.commit()

    except Exception as err:
        print(f'Erro na execução da query: {err}')
    connection.close()

    return resultado