#(Cmpn_name, Sctr_name, EPS, P/E, Close_price, Report_date)

from mysql.connector import MySQLConnection, Error
from py_mysql_config import read_db_config

def insert_cmpn_names(names):

    db_config = read_db_config()
    query = 'INSERT INTO Companies (Cmpn_name) VALUES (%s)'
    try:
        cnnct = MySQLConnection(**db_config)
        cursor = cnnct.cursor()
        cursor.executemany(query, names)

        cnnct.commit()
    except Error as e:
        print("\nOooops.... Something went wrong.... Maby this:\n")
        print(e)
    finally:
        cursor.close()
        cnnct.close()

def main():
    Cmpn_name1 = input("What's first company Name? ")
    Cmpn_name2 = input("What's second company Name? ")
    Cmpn_name3 = input("What's third company Name? ")
    note_lst = [Cmpn_name1, Cmpn_name2, Cmpn_name3]

    insert_cmpn_names(note_lst)

if __name__ == '__main__':
    main()
