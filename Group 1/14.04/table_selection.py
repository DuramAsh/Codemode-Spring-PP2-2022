import psycopg2

config = psycopg2.connect(
    host='localhost',
    database='postgres',
    user='postgres',
    password='Ebalokratosa.228'
)

current = config.cursor()


# sql = '''
# 	SELECT company_name FROM works WHERE person_name = 'yaslan';
# '''
# sql = '''
# 	SELECT * FROM works ORDER BY salary DESC;
# '''
sql = '''
	SELECT DISTINCT employee.person_name, company.company_name
FROM employee,
     works,
     company
WHERE employee.city = company.city
  AND works.company_name = company.company_name
  AND works.person_name = employee.person_name;
'''


current.execute(sql)

final = current.fetchall()
print(final)

current.close()
# config.commit()
config.close()
