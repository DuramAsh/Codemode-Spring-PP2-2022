import psycopg2

config = psycopg2.connect(
    host='localhost',
    database='postgres',
    port=5432,
    user='postgres',
    password='Adil2002'
)

current = config.cursor()

try:
    user_id = input("Enter ID: ")
    to_change = input("What do you want to change?: ")
    data = input("To what value set the old value?: ")
    to_change = to_change.lower()
    if to_change == 'username':
        sql = '''
            UPDATE phonebook SET username = %s WHERE id = %s;
        '''
    elif to_change == 'number':
        sql = '''
            UPDATE phonebook SET number = %s WHERE id = %s;
        '''
    current.execute(sql, (data, user_id))
    config.commit()
except:
    print("ERROR!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

current.close()
config.close()
