
import sqlite3 as conector

# Programa de Notas de Alunos

def criar_tabela():
    try:
        # Abertura de conexão e aquisição de cursor
        conexao = conector.connect("./meu_banco.db")
        cursor = conexao.cursor()

        # Execução de um comando: CREATE TABLE Aluno e Nota
        comando_aluno = '''CREATE TABLE IF NOT EXISTS Aluno (
                            aluno_id INTEGER PRIMARY KEY AUTOINCREMENT,
                            nome TEXT NOT NULL
                            );'''
        comando_nota = '''CREATE TABLE IF NOT EXISTS Nota (
                           id INTEGER PRIMARY KEY AUTOINCREMENT,
                           aluno_id INTEGER NOT NULL,
                           disciplina TEXT NOT NULL,
                           nota REAL NOT NULL,
                           FOREIGN KEY (aluno_id) REFERENCES Aluno (aluno_id) ON DELETE CASCADE
                           );'''
        cursor.execute(comando_aluno)
        cursor.execute(comando_nota)

        # Efetivação dos comandos
        conexao.commit()

        print("Tabelas Criadas Com Sucesso.")

    except conector.DatabaseError as err:
        print("Erro de banco de dados", err)

    finally:
        # Fechamento das conexões
        if conexao:
            cursor.close()
            conexao.close()

def inserir_aluno():
    try:
        # Abertura de conexão e aquisição de cursor
        conexao = conector.connect("./meu_banco.db")
        cursor = conexao.cursor()

        # Perguntar o nome do Aluno
        nome = input("Digite o nome do aluno: \n")

        # Definição de um comando com query parameter
        comando = '''INSERT INTO Aluno (nome) VALUES (?);'''
        cursor.execute(comando, (nome,))

        # Efetivação do comando
        conexao.commit()

        print("Aluno Inserido Com Sucesso.")

    except conector.DatabaseError as err:
        print("Erro de banco de dados", err)

    finally:
        # Fechamento das conexões
        if conexao:
            cursor.close()
            conexao.close()

def inserir_nota():
    try:
        # Abertura de conexão e aquisição de cursor
        conexao = conector.connect("./meu_banco.db")
        cursor = conexao.cursor()

        # Perguntar os dados da Nota
        aluno_id = int(input("Digite o ID do aluno: \n"))
        disciplina = input("Digite a disciplina: \n")
        nota = float(input("Digite a nota: \n"))

        # Definição de um comando com query parameter
        comando = '''INSERT INTO Nota (aluno_id, disciplina, nota) VALUES (?, ?, ?);'''
        cursor.execute(comando, (aluno_id, disciplina, nota))

        # Efetivação do comando
        conexao.commit()

        print("Nota Inserida Com Sucesso.")

    except conector.DatabaseError as err:
        print("Erro de banco de dados", err)

    finally:
        # Fechamento das conexões
        if conexao:
            cursor.close()
            conexao.close()


def remover_aluno():
    try:
        # Abertura de conexão e aquisição de cursor
        conexao = conector.connect("./meu_banco.db")
        conexao.execute("PRAGMA foreign_keys = on")
        cursor = conexao.cursor()

        # Perguntando o ID do aluno a ser removido
        aluno_id = int(input("Digite o ID do aluno a ser removido: \n"))

        # Definição dos comandos
        comando = '''DELETE FROM Aluno WHERE aluno_id = ?;'''
        cursor.execute(comando, (aluno_id,))

        # Efetivação do comando
        conexao.commit()

        print("Aluno Removido Com Sucesso.")

    except conector.DatabaseError as err:
        print("Erro de banco de dados", err)

    finally:
        # Fechamento das conexões
        if conexao:
            cursor.close()
            conexao.close()

def remover_nota():
    try:
        # Abertura de conexão e aquisição de cursor
        conexao = conector.connect("./meu_banco.db")
        conexao.execute("PRAGMA foreign_keys = on")
        cursor = conexao.cursor()

        # Perguntando o ID do aluno para exibir as notas
        aluno_id = int(input("Digite o ID do aluno para remover uma nota: \n"))

        # Exibe as notas do aluno
        comando = '''SELECT id, disciplina, nota FROM Nota WHERE aluno_id = ?;'''
        cursor.execute(comando, (aluno_id,))
        registros = cursor.fetchall()

        if registros:
            print(f"Notas do Aluno (ID: {aluno_id}):")
            for registro in registros:
                print(f"ID da Nota: {registro[0]}, Disciplina: {registro[1]}, Nota: {registro[2]}")

            # Pergunta o ID da nota a ser removida
            nota_id = int(input("Digite o ID da nota a ser removida: \n"))

            # Verifica se a nota pertence ao aluno
            nota_ids = [registro[0] for registro in registros]
            if nota_id in nota_ids:
                # Definição dos comandos
                comando = '''DELETE FROM Nota WHERE id = ?;'''
                cursor.execute(comando, (nota_id,))

                # Efetivação do comando
                conexao.commit()
                print("Nota Removida Com Sucesso.")
            else:
                print("ID da Nota inválido para o aluno especificado.")
        else:
            print("Nenhuma nota encontrada para o aluno com ID:", aluno_id)

    except conector.DatabaseError as err:
        print("Erro de banco de dados", err)

    finally:
        # Fechamento das conexões
        if conexao:
            cursor.close()
            conexao.close()

def alterar_nota():
    try:
        # Abertura de conexão e aquisição de cursor
        conexao = conector.connect("./meu_banco.db")
        conexao.execute("PRAGMA foreign_keys = on")
        cursor = conexao.cursor()

        # Pergunta o ID do aluno para exibir as notas
        aluno_id = int(input("Digite o ID do aluno para alterar uma nota: \n"))

        # Exibir as notas do aluno
        comando = '''SELECT id, disciplina, nota FROM Nota WHERE aluno_id = ?;'''
        cursor.execute(comando, (aluno_id,))
        registros = cursor.fetchall()

        if registros:
            print("Notas do Aluno (ID: {}):".format(aluno_id))
            for registro in registros:
                print("ID da Nota: {}, Disciplina: {}, Nota: {}".format(registro[0], registro[1], registro[2]))

            # Pergunta o ID da nota a ser alterada
            nota_id = int(input("Digite o ID da nota a ser alterada: \n"))

            # Verifica se a nota pertence ao aluno
            nota_ids = [registro[0] for registro in registros]
            if nota_id in nota_ids:
                # Pergunta a nova nota
                nova_nota = float(input("Digite a nova nota: \n"))

                # Definição do comando
                comando = '''UPDATE Nota SET nota = ? WHERE id = ?;'''
                cursor.execute(comando, (nova_nota, nota_id))

                # Efetivação do comando
                conexao.commit()
                print("Nota Alterada Com Sucesso.")
            else:
                print("ID da Nota inválido para o aluno especificado.")
        else:
            print("Nenhuma nota encontrada para o aluno com ID:", aluno_id)

    except conector.DatabaseError as err:
        print("Erro de banco de dados", err)

    finally:
        # Fechamento das conexões
        if conexao:
            cursor.close()
            conexao.close()

def consultar_alunos():
    try:
        # Abertura de conexão e aquisição de cursor
        conexao = conector.connect("./meu_banco.db")
        cursor = conexao.cursor()

        # Definição do comando de consulta
        comando = '''SELECT * FROM Aluno;'''
        cursor.execute(comando)

        # Recuperação dos dados
        registros = cursor.fetchall()
        print("Tipo retornado pelo fetchall():", type(registros))

        for registro in registros:
            print("Tipo:", type(registro), "- Conteúdo:", registro)

        print("Dados dos Alunos Consultados Com Sucesso.")

    except conector.DatabaseError as err:
        print("Erro de banco de dados", err)

    finally:
        # Fechamento das conexões
        if conexao:
            cursor.close()
            conexao.close()

def consultar_notas():
    try:
        # Abertura de conexão e aquisição de cursor
        conexao = conector.connect("./meu_banco.db")
        cursor = conexao.cursor()

        # Pergunta o ID do aluno para consulta
        aluno_id = int(input("Digite o ID do aluno para consultar as notas: \n"))

        # Definição do comando de consulta
        comando = '''SELECT id, disciplina, nota FROM Nota WHERE aluno_id = ?;'''
        cursor.execute(comando, (aluno_id,))

        # Recuperação dos dados
        registros = cursor.fetchall()

        if registros:
            print("Notas do Aluno (ID: {}):".format(aluno_id))
            for registro in registros:
                print("ID da Nota: {}, Disciplina: {}, Nota: {}".format(registro[0], registro[1], registro[2]))
        else:
            print("Não há notas para o aluno com ID:", aluno_id)

        print("Notas Consultadas Com Sucesso.")

    except conector.DatabaseError as err:
        print("Erro de banco de dados", err)

    finally:
        # Fechamento das conexões
        if conexao:
            cursor.close()
            conexao.close()

# Programa Principal

while True:
    opcao = input('''Programa de Registro de Notas\n
    1 - Criar Tabelas\n
    2 - Inserir Aluno\n
    3 - Inserir Nota\n
    4 - Remover Aluno\n
    5 - Remover Nota\n
    6 - Alterar Nota\n
    7 - Consultar Alunos\n
    8 - Consultar Notas\n
    9 - Terminar Programa\n
    Digite uma opção: ''')

    if opcao == "1":
        criar_tabela()
    elif opcao == "2":
        inserir_aluno()
    elif opcao == "3":
        inserir_nota()
    elif opcao == "4":
        remover_aluno()
    elif opcao == "5":
        remover_nota()
    elif opcao == "6":
        alterar_nota()
    elif opcao == "7":
        consultar_alunos()
    elif opcao == "8":
        consultar_notas()
    elif opcao == "9":
        print("Fim da Execução do Programa.")
        break
    else:
        print("Opção Inválida.\n")