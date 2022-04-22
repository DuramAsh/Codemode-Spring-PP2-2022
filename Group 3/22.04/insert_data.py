import psycopg2,csv
from config import data
config = psycopg2.connect(**data)

current = config.cursor()

sql = """
    INSERT INTO PhoneBook VALUES(%s,%s,%s) returning *;
"""

try:
    result = []
    with open("PhoneBook.csv", "r") as f:
        reader = csv.reader(f, delimiter=",")
        for row in reader:
            current.execute(sql, row)
            result.append(current.fetchone())
    print(result)
except Exception as e:
    name = input("Enter the name:")
    phoneNumber = input("Enter the number:")
    city = input("Enter the city:")
    current.execute(sql, (name,phoneNumber,city))
    print(current.fetchone())

current.close()
config.commit()
config.close()