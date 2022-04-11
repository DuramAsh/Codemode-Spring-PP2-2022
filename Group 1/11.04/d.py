import psycopg2

config = psycopg2.connect(
    host='localhost', 
    database='postgres',
    user='postgres',
    password='Adil2002'
)

current = config.cursor()


sql = '''
    UPDATE users 
    SET age = %s, information = %s
    WHERE username=%s RETURNING *
'''

current.execute(sql, (200, 'Not Cobalt, but Codemode', 'Jaks'))

final = current.fetchone()
print(final)



current.close()

config.commit()
config.close()