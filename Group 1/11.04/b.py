import psycopg2

config = psycopg2.connect(
    host='localhost', 
    database='postgres',
    user='postgres',
    password='Adil2002'
)

current = config.cursor()

current.execute(
    '''
    CREATE TABLE users(
        username VARCHAR(255),
        age INTEGER,
        registration_date DATE,
        information TEXT,
        password VARCHAR(50)
    );
    '''
)




current.close()

config.commit()
config.close()