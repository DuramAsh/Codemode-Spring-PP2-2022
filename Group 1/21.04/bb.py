import psycopg2

conn = psycopg2.connect(
    host='localhost', 
    database='postgres',
    port=5432,
    user='postgres',
    password='Adil2002'
)

cursor = conn.cursor()



name = str(input("Name: "))
cursor.callproc('getStudentNameSurnamePhone', [name])
print(cursor.fetchall())


cursor.close()
conn.commit()
conn.close()

