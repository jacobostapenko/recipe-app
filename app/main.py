import psycopg2
#connection to server
connection = psycopg2.connect(host='localhost', port="5432",
 database="master", user="postgres",password="password")

def connect():
    try:
        print('connecting to sql server...')
        cursor = connection.cursor()
        print('db version:')

        #selecting/printing postgres version, test
        cursor.execute('SELECT version()')
        db_version = cursor.fetchone()
        print(db_version)
        cursor.close()
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        connection.close()
        print('database connection closed')

if __name__ == '__main__':
    connect()