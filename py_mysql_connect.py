from mysql.connector import MySQLConnection, Error
from py_mysql_config import read_db_config

def connect():
    """Connect to MySQL database"""

    db_config = read_db_config()

    try:
        print('Connecting to MySQL database...')
        cnnct = MySQLConnection(**db_config)

        if cnnct.is_connected():
            print('Connection established.')
        else:
            print('Connection failed.')
    except Error as error:
        print(error)

    finally:
        cnnct.close()
        print('Connection closed.')

if __name__ == '__main__':
    connect()
