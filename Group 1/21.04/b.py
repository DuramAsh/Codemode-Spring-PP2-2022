import psycopg2

config = psycopg2.connect(
    host='localhost', 
    database='postgres',
    port=5432,
    user='postgres',
    password='Adil2002'
)

current = config.cursor()

id = 1
username = 'Adil'
number = '87088341979'
email = 'adilzhapar2002@gmail.com'

sql = '''
    INSERT INTO phonebook
    VALUES (%s, %s, %s, %s);
'''

current.execute(sql, (id, username, number, email))


config.commit()
current.close()
config.close()