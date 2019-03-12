#Updating whole notes in Companies table

from mysql.connector import MySQLConnection, Error
from py_mysql_config import read_db_config

def update_names(names):
    db_config = read_db_config()
    query = 'UPDATE Companies SET Cmpn_name = %s WHERE idCmpn = %s'
    try:
        cnnct = MySQLConnection(**db_config)
        cursor = cnnct.cursor()

        max_in_key_lst = len(names)+10 #Counting starts from 10 and ends '10 + elements amount' because of working MySQL table features. There is no need in this '+10' for new_database in new project
        key_lst = [i for i in range(10, max_in_key_lst)]
        query_lst_inp = []
        item = None
        for i in range(0, len(names)):
            item = (names[i], str(key_lst[i]))
            query_lst_inp.append(item)

        cursor.executemany(query, query_lst_inp)
        cnnct.commit()
        print('\nCongrads! Table updated ;)\n')
    except Error as e:
        print('\nOoops... Sorry, something went wrong... Maybe this:\n')
        print(e)
    finally:
        cursor.close()
        cnnct.close()
def main():
    print("\nWell, you want to update companies names. Here we go!\n")

    Cmpn_name1 = input('Print first company name: ')
    Cmpn_name2 = input('Pint second company name: ')
    Cmpn_name3 = input('Print the third company name: ')

    names = [Cmpn_name1, Cmpn_name2, Cmpn_name3]

    update_names(names)
if __name__ == '__main__':
    main()
