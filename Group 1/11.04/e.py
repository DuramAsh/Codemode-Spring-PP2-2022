import psycopg2

config = psycopg2.connect(
    host='localhost', 
    database='postgres',
    user='postgres',
    password='Adil2002'
)

current = config.cursor()


sql = '''
    SELECT username, age, password FROM users ORDER BY username DESC
'''

sql2 = '''
    SELECT username, age, password FROM users ORDER BY username ASC
'''

current.execute(sql2)


final = current.fetchall()
print(final)



current.close()

config.commit()
config.close()