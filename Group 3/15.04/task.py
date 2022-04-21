import psycopg2
from config import data
config = psycopg2.connect(**data)

current = config.cursor()

insert_e = 'INSERT INTO employee VALUES (%s, %s, %s);'
insert_c = 'INSERT INTO company VALUES (%s, %s);'
insert_w = 'INSERT INTO works VALUES (%s, %s, %s);'

current.execute(insert_e, ('Morti', 'Bonjour', 'Paris'))
current.execute(insert_e, ('Lyaka', 'Al farabi', 'Almaty'))
current.execute(insert_e, ('Dias', 'Sholoxova', 'Uralsk'))
current.execute(insert_e, ('Alina', 'Green', 'Tel aviv'))
current.execute(insert_e, ('Akmira', 'Amore', 'Paris'))
current.execute(insert_e, ('Aldiar', 'Pushkin', 'Almaty'))
current.execute(insert_e, ('Alikhan', 'Stroitel', 'Uralsk'))
current.execute(insert_e, ('Dinara', 'Red square', 'New York'))
current.execute(insert_e, ('Nura', 'Arbat', 'Aktue'))

current.execute(insert_c, ('Choco', 'Almaty'))
current.execute(insert_c, ('KBTU', 'Almaty'))
current.execute(insert_c, ('Coca Cola', 'New York'))
current.execute(insert_c, ('Dior', 'Paris'))
current.execute(insert_c, ('PlayBoy', 'Paris'))
current.execute(insert_c, ('Google', 'Uralsk'))
current.execute(insert_c, ('Meta', 'Tel aviv'))
current.execute(insert_c, ('Jubanov', 'Aktue'))

current.execute(insert_w, ('Alikhan','Google','50000'))
current.execute(insert_w, ('Morti','PlayBoy','1'))
current.execute(insert_w, ('Dias','Jubanov','10000'))
current.execute(insert_w, ('Lyaka','Coca Cola','1000000'))
current.execute(insert_w, ('Akmira','Dior','50000'))
current.execute(insert_w, ('Alina','Meta','100000'))
current.execute(insert_w, ('Aldiar','KBTU','31500'))
current.execute(insert_w, ('Dinara','Coca Cola','1000000'))
current.execute(insert_w, ('Nura','PlayBoy','2'))

get = '''
    SELECT employee.person_name, company.company_name, employee.city FROM employee, company, works
    WHERE works.person_name = employee.person_name and
          works.company_name = company.company_name and
          employee.city = company.city;

    SELECT * from works WHERE salary > 90000 ORDER BY salary ASC ;
'''

current.close()
config.commit()
config.close()  