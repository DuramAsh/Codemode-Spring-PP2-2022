import psycopg2
from config import data
config = psycopg2.connect(**data)

current = config.cursor()

sql = """
    SELECT * FROM PhoneBook;
"""
current.execute(sql)

print(*current.fetchall(), sep='\n')

current.close()
config.commit()
config.close()