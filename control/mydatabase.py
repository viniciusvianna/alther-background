import mysql.connector
import control.parser as parser

config = {
    'user': 'root',
    'password': 'Kvothe1807',
    'host': 'localhost',
    'database': 'alther_battleground',
    'raise_on_warnings': True
}


def open_connection():
    mydb = mysql.connector.connect(**config)
    return mydb


def create_cursor(connection):
    cursor = connection.cursor()
    return cursor


def close_connection(cursor, connection):
    cursor.close()
    connection.close()


def get_character_by_id(char_id):
    query = "SELECT DETALHES FROM PERSONAGENS WHERE ID_PERSONAGEM = %s"
    val = (char_id,)
    connection = open_connection()
    cursor = create_cursor(connection)

    cursor.execute(query, val)

    result = parser.parse_character_json(cursor.fetchone()[0], char_id)

    close_connection(cursor, connection)

    return result
