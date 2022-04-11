import psycopg2

config = psycopg2.connect(
    host='localhost', 
    database='postgres',
    user='postgres',
    password='Adil2002'
)

current = config.cursor()

current.execute('SELECT version();')

db_version = current.fetchall()


print("Psql version:")
print(db_version)

current.close()
config.close()