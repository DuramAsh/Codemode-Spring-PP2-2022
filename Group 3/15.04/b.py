import psycopg2
from config import data
config = psycopg2.connect(**data)

current = config.cursor()

create_table = '''
CREATE TABLE Retaked_students(
     
)

'''

current.execute()

db_version = current.fetchall()


print("Psql version:")
print(db_version)

current.close()
config.close()