import psycopg2

config = psycopg2.connect(
    host='localhost', 
    database='postgres',
    port=5432,
    user='postgres',
    password='Adil2002'
)

current = config.cursor()

current.execute(
    '''
    CREATE TABLE phonebook(
        id INTEGER PRIMARY KEY,
        username VARCHAR(20),
        number INTEGER,
        email VARCHAR(30)
    )
    '''
)

config.commit()
current.close()
config.close()