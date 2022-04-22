import psycopg2,csv
from config import data
config = psycopg2.connect(**data)

current = config.cursor()

sql = """
    DELETE FROM PhoneBook WHERE person_name = %s;
"""

name = input()

current.execute(sql, (name,))

current.close()
config.commit()
config.close()