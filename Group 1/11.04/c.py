import psycopg2

config = psycopg2.connect(
    host='localhost', 
    database='postgres',
    user='postgres',
    password='Adil2002'
)

current = config.cursor()


sql = '''
    INSERT INTO users VALUES (%s, %s, %s, %s, %s) RETURNING *
'''

username = 'Adil'
age = 19
registration_date = '11.04.2022'
info = 'Old man, take a look at my life.'
password = '12345'


current.execute(sql, (username, age, registration_date, info, password))

final = current.fetchall()
print(*final)

current.close()

config.commit()
config.close()