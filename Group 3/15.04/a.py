import psycopg2
from config import data
config = psycopg2.connect(**data)

current = config.cursor()

current.execute('SELECT version();')

db_version = current.fetchall()


print("Psql version:")
print(db_version)

current.close()
config.close()