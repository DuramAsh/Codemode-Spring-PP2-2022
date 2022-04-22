import psycopg2
from config import data
config = psycopg2.connect(**data)

current = config.cursor()

sql = """
    UPDATE PhoneBook SET phone_number = %s WHERE person_name = %s;
"""

name = input()
phone_number = input()

current.execute(sql, (phone_number,name))

current.close()
config.commit()
config.close()