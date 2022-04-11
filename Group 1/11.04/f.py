import psycopg2

config = psycopg2.connect(
    host='localhost', 
    database='postgres',
    user='postgres',
    password='Adil2002'
)

current = config.cursor()


sql = '''
    DELETE FROM users WHERE username = %s RETURNING *
'''

current.execute(sql, ('Adil',))



final = current.fetchall()
print(final)



current.close()

config.commit()
config.close()