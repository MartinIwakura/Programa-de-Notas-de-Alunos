# Programa de um Sistema de Notas de Alunos

import sqlite3 as conector

def criar_tabela():
    try:
        # Abertura de conexão e aquisição de cursor
        conexao = conector.connect("./meu_banco.db")
        cursor = conexao.cursor()

        # Criando as tabelas Aluno E Nota
        comando_aluno = '''CREATE TABLE IF NOT EXISTS Aluno (
                            aluno_cpf INTEGER PRIMARY KEY,
                            nome TEXT NOT NULL,
                            email TEXT
                            );'''
        comando_nota = '''CREATE TABLE IF NOT EXISTS Nota (
                           id INTEGER PRIMARY KEY AUTOINCREMENT,
                           aluno_cpf INTEGER NOT NULL,
                           disciplina TEXT NOT NULL,
                           nota REAL NOT NULL,
                           FOREIGN KEY (aluno_cpf) REFERENCES Aluno (aluno_cpf) ON DELETE CASCADE
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

        # Perguntar os dados do Aluno (como cpf, nome e email)
        cpf = input("Digite o CPF do aluno: \n")
        nome = input("Digite o nome do aluno: \n")
        email = input("Digite o email do aluno: \n")

        # Definição de um comando com query parameter
        comando = '''INSERT INTO Aluno (aluno_cpf, nome, email) VALUES (?, ?, ?);'''
        cursor.execute(comando, (cpf, nome, email))

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
        aluno_cpf = int(input("Digite o CPF do aluno: \n"))
        disciplina = input("Digite a disciplina: \n")
        nota = float(input("Digite a nota: \n"))

        # Definição de um comando com query parameter
        comando = '''INSERT INTO Nota (aluno_cpf, disciplina, nota) VALUES (?, ?, ?);'''
        cursor.execute(comando, (aluno_cpf, disciplina, nota))

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
        aluno_cpf = int(input("Digite o CPF do aluno a ser removido: \n"))

        # Definição dos comandos
        comando = '''DELETE FROM Aluno WHERE aluno_cpf = ?;'''
        cursor.execute(comando, (aluno_cpf,))

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

def alterar_dados():
    try:
        # Abertura de conexão e aquisição de cursor
        conexao = conector.connect("./meu_banco.db")
        cursor = conexao.cursor()

        # Perguntando o CPF do aluno cujos dados serão alterados
        aluno_cpf = input("Digite o CPF do aluno cujos dados serão alterados: \n")

        # Perguntando o novo nome, CPF e email do aluno
        novo_nome = input("Digite o novo nome do aluno: \n")
        novo_cpf = input("Digite o novo CPF do aluno: \n")
        novo_email = input("Digite o novo Email do aluno: \n")

        # Definição do comando de atualização
        comando = '''UPDATE Aluno SET nome = ?, aluno_cpf = ?, email =? WHERE aluno_cpf = ?;'''
        cursor.execute(comando, (novo_nome, novo_cpf, novo_email, aluno_cpf))

        # Efetivação do comando
        conexao.commit()

        print("Dados do aluno atualizados com sucesso.")

    except conector.DatabaseError as err:
        print("Erro de banco de dados:", err)

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

        # Perguntando o CPF do aluno para exibir as notas
        aluno_cpf = int(input("Digite o CPF do aluno para remover uma nota: \n"))

        # Exibe as notas do aluno
        comando = '''SELECT id, disciplina, nota FROM Nota WHERE aluno_cpf = ?;'''
        cursor.execute(comando, (aluno_cpf,))
        registros = cursor.fetchall()

        if registros:
            print(f"Notas do Aluno (ID: {aluno_cpf}):")
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
            print("Nenhuma nota encontrada para o aluno com CPF:", aluno_cpf)

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

        # Pergunta o CPF do aluno para exibir as notas
        aluno_cpf = int(input("Digite o CPF do aluno para alterar uma nota: \n"))

        # Exibir as notas do aluno
        comando = '''SELECT id, disciplina, nota FROM Nota WHERE aluno_cpf = ?;'''
        cursor.execute(comando, (aluno_cpf,))
        registros = cursor.fetchall()

        if registros:
            print("Notas do Aluno (CPF: {}):".format(aluno_cpf))
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
            print("Nenhuma nota encontrada para o aluno com ID:", aluno_cpf)

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
        comando = '''SELECT aluno_cpf, nome, email FROM Aluno;'''
        cursor.execute(comando)

        # Recuperação dos dados
        registros = cursor.fetchall()
        print("Tipo retornado pelo fetchall():", type(registros))

        for registro in registros:
            cpf = registro[0]
            nome = registro[1]
            email = registro[2]
            print("Cpf:", cpf, "- Nome:", nome, "- Email:", email)

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

        # Pergunta o CPF do aluno para consulta
        aluno_cpf = int(input("Digite o CPF do aluno para consultar as notas: \n"))

        # Definição do comando de consulta
        comando = '''SELECT id, disciplina, nota FROM Nota WHERE aluno_cpf = ?;'''
        cursor.execute(comando, (aluno_cpf,))

        # Recuperação dos dados
        registros = cursor.fetchall()

        if registros:
            print("Notas do Aluno (CPF: {}):".format(aluno_cpf))
            for registro in registros:
                print("ID da Nota: {}, Disciplina: {}, Nota: {}".format(registro[0], registro[1], registro[2]))
        else:
            print("Não há notas para o aluno com ID:", aluno_cpf)

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
    6 - Alterar Dados\n
    7 - Alterar Nota\n
    8 - Consultar Alunos\n
    9 - Consultar Notas\n
    0 - Terminar Programa\n
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
        alterar_dados()
    elif opcao == "7":
        alterar_nota()
    elif opcao == "8":
        consultar_alunos()
    elif opcao == "9":
        consultar_notas()
    elif opcao == "0":
        print("Fim da Execução do Programa.")
        break
    else:
        print("Opção Inválida.\n")
