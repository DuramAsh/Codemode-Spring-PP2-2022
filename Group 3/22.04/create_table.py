import psycopg2
from config import data
config = psycopg2.connect(**data)

current = config.cursor()

sql = """
    CREATE TABLE users(
        user_name VARCHAR,
        score INT DEFAULT(0), 
        level INT DEFAULT(0)
    );
"""

current.execute(sql)

current.close()
config.commit()
config.close()