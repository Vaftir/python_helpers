# Autor: Yago Assis Mendes Faria
import mysql.connector
from mysql.connector import Error

'''
 Modulo de conexão com o banco de dados MySQL

    Atributos:
        host: str
        database: str
        user: str
        password: str
        connection: mysql.connector.connection.MySQLConnection
        cursor: mysql.connector.cursor.MySQLCursor
    Métodos:
        connect: bool
        execute_query: bool
        execute_read_query: list
        disconnect: bool
        __enter__: Connection
        __exit__: None
    dependencias:
        mysql.connector
        mysql.connector.Error
    
'''
class Connection:
    def __init__(self, host, database, user, password):
        self.connection = None
        self.cursor = None
        self.host = host
        self.database = database
        self.user = user
        self.password = password

    def connect(self):
        # Conecta ao banco de dados
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            self.cursor = self.connection.cursor()
            print("Connected to MySQL database")
            return True
        except Error as e:
            print(f"The error '{e}' occurred")
            return False

    def execute_query(self, query, params=None):
        # Executa uma query no banco de dados
        try:
            self.cursor.execute(query, params)
            self.connection.commit()
            print("Query executed successfully")
            return True
        except Error as e:
            print(f"The error '{e}' occurred")
            return False

    def execute_read_query(self, query, params=None):
        # Executa uma query de leitura no banco de dados
        result = None
        try:
            self.cursor.execute(query, params)
            result = self.cursor.fetchall()
            return result
        except Error as e:
            print(f"The error '{e}' occurred")
            return result

    def disconnect(self):
        # Desconecta do banco de dados
        if self.connection is not None and self.connection.is_connected():
            self.cursor.close()
            self.connection.close()
            print("Connection closed")
            return True
        else:
            print("No connection to close")
            return False

    def __enter__(self):
        # Entra no contexto da classe
        if self.connect():
            return self
        else:
            raise Exception("Failed to connect to the database")

    def __exit__(self, exc_type, exc_val, exc_tb):
        # Sai do contexto da classe
        self.disconnect()


'''
# Exemplo de uso da classe de conexão
# Importando a classe de conexão
from connection import Connection

# Criando uma instância da classe de conexão
connection = Connection("localhost",
'''