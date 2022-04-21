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

sql = '''
    INSERT INTO phonebook
    VALUES (%s, %s, %s, %s);
'''

try:
    with open('a.csv') as f:
        reader = csv.reader(f, delimiter=',')
        
        for row in reader:
            # print(type(row))
            # print(row)
            row[0] = int(row[0])
            arr.append(row)
    for row in arr:
        current.execute(sql, row)    
except:
    print("ID:")
    id = int(input())
    print("Username:")
    username = input()
    print("Phone number:")
    number = input()
    print("E-mail:")
    email = input()
    current.execute(sql, (id, username, number, email))

current.close()
config.commit()
config.close()
