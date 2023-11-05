import mysql.connector
from mysql.connector import Error

class SQL:
    def __init__(self):
        # Conectar ao banco de dados
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="admin",
            database="academia"
        )
        self.mycursor = self.mydb.cursor()

    def cadastrar_usuario(self, Usuario, Idade, Sexo, Endereço, Telefone):
            # Verificar se o e-mail já foi cadastrado antes
            sql = "SELECT * FROM clientes WHERE Nome = %s"
            val = (Usuario, )

            self.mycursor.execute(sql, val)

            conta_existente = self.mycursor.fetchone()

            if conta_existente:
                print("O e-mail já foi cadastrado. Tente novamente com outro endereço de e-mail.")
                return

            # Inserir a nova conta no banco de dados
            sql = "INSERT INTO clientes (Nome, Idade, Sexo, Endereco, Telefone) VALUES (%s, %s, %s, %s, %s)"
            val = (Usuario, Idade, Sexo, Endereço, Telefone)

            self.mycursor.execute(sql, val)

            self.mydb.commit()

            print("Conta criada com sucesso!")

    def cadastrar_treinadores(self, Usuario, Especializacao, Experiencia, NumeroRegistro):
            # Verificar se o e-mail já foi cadastrado antes
            sql = "SELECT * FROM treinadores WHERE Nome = %s"
            val = (Usuario, )

            self.mycursor.execute(sql, val)

            conta_existente = self.mycursor.fetchone()

            if conta_existente:
                print("O e-mail já foi cadastrado. Tente novamente com outro endereço de e-mail.")
                return

            # Inserir a nova conta no banco de dados
            sql = "INSERT INTO treinadores (Nome, Especializacao, Experiencia, NumeroRegistro) VALUES (%s, %s, %s, %s)"
            val = (Usuario, Especializacao, Experiencia, NumeroRegistro)

            self.mycursor.execute(sql, val)

            self.mydb.commit()

            print("Conta criada com sucesso!")

    def buscar_tabela(self, Tabela):
        try:
            sql = "SELECT * FROM " + Tabela
            self.mycursor.execute(sql)
            resultado = self.mycursor.fetchall()
            text = ''

            for registro in resultado:
                text += str(registro) + '\n'
            
            return text
        
        except Error as e:
            if "Table" in str(e) and "doesn't exist" in str(e):
                print(f"A tabela '{Tabela}' não existe no banco de dados.")
            else:
                print("Ocorreu um erro ao acessar o banco de dados:", str(e))
            return ''  
        
    def buscar_usuarios(self, user, table):
            sql = "SELECT * FROM " + table + " WHERE Nome = %s"
            val = (user, )

            self.mycursor.execute(sql, val)

            user = self.mycursor.fetchone()
            return user

    def update_usuario(self, Usuario, Idade, Sexo, Endereço, Telefone):
        # Verificar se o e-mail já foi cadastrado antes
        sql = "SELECT * FROM clientes WHERE Nome = %s"
        val = (Usuario, )

        self.mycursor.execute(sql, val)

        conta_existente = self.mycursor.fetchone()

        if conta_existente:
            # Inserir a nova conta no banco de dados
            
            sql = "UPDATE clientes SET Nome = %s, Idade = %s, Sexo = %s, Endereco = %s, Telefone = %s WHERE Nome = %s"
            val = (Usuario ,Idade, Sexo, Endereço, Telefone, Usuario)

            self.mycursor.execute(sql, val)
            self.mydb.commit()

            print("O usuario foi atualizado")
        else:
            print("O usuario sitado não existe. Tente novamente com outro nome.")
         
    def update_treinadores(self, Usuario, Especializacao, Experiencia, NumeroRegistro):
        # Verificar se o e-mail já foi cadastrado antes
        sql = "SELECT * FROM treinadores WHERE Nome = %s"
        val = (Usuario, )

        self.mycursor.execute(sql, val)

        conta_existente = self.mycursor.fetchone()

        if conta_existente:
            # Inserir a nova conta no banco de dados
            
            sql = "UPDATE treinadores SET Nome = %s, Especializacao = %s, Experiencia = %s, NumeroRegistro = %s WHERE Nome = %s"
            val = (Usuario ,Especializacao, Experiencia, NumeroRegistro, Usuario)

            self.mycursor.execute(sql, val)
            self.mydb.commit()

            print("O usuario foi atualizado")
        else:
            print("O usuario sitado não existe. Tente novamente com outro nome.")
         
    def delete_field(self, table, ID):
        # Verificar se o e-mail já foi cadastrado antes
        sql = f"SELECT * FROM {table} WHERE ID = %s"
        val = (ID,)
        self.mycursor.execute(sql, val)

        conta_existente = self.mycursor.fetchone()

        if conta_existente:
            sql = f"DELETE FROM {table} WHERE ID = %s"
            val = (ID,)

            self.mycursor.execute(sql, val)
            self.mydb.commit()

            print("O usuario foi exluido")
        else:
            print("O usuario sitado não existe. Tente novamente com outro ID.")
         
    def cadastrar_conta(self, nome, email, senha):
            # Verificar se o e-mail já foi cadastrado antes
            sql = "SELECT * FROM contas WHERE email = %s"
            val = (email, )

            self.mycursor.execute(sql, val)

            conta_existente = self.mycursor.fetchone()

            if conta_existente:
                print("O e-mail já foi cadastrado. Tente novamente com outro endereço de e-mail.")
                return

            # Inserir a nova conta no banco de dados
            sql = "INSERT INTO contas (nome, email, senha) VALUES (%s, %s, %s)"
            val = (nome, email, senha)

            self.mycursor.execute(sql, val)

            self.mydb.commit()

            print("Conta criada com sucesso!")

    def login(self, email, senha):
        # Verificar se a conta existe no banco de dados
        sql = "SELECT * FROM contas WHERE email = %s AND senha = %s"
        val = (email, senha)

        self.mycursor.execute(sql, val)

        conta = self.mycursor.fetchone()

        if conta:
            print("Bem-vindo,", conta[1])
            return True
        else:
            print("E-mail ou senha incorretos. Tente novamente.")
            return False

    def close(self):
        self.mydb.close()


