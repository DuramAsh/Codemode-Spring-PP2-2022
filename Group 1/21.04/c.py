import csv, psycopg2

config = psycopg2.connect(
    host='localhost', 
    database='postgres',
    port=5432,
    user='postgres',
    password='Adil2002'
)

current = config.cursor()
arr = []

with open('a.csv') as f:
    reader = csv.reader(f, delimiter=',')
    
    for row in reader:
        # print(type(row))
        # print(row)
        row[0] = int(row[0])
        arr.append(row)

sql = '''
    INSERT INTO phonebook
    VALUES (%s, %s, %s, %s) RETURNING *;
'''

for row in arr:
    current.execute(sql, row)

final = current.fetchall()
print(final)

current.close()
config.commit()
config.close()