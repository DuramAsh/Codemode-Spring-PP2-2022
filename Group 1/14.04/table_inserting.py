import psycopg2

config = psycopg2.connect(
    host='localhost',
    database='postgres',
    user='postgres',
    password='Ebalokratosa.228'
)

current = config.cursor()


sql = '''
	INSERT INTO employee VALUES ('Aibergen', 'Momyshuly 12', 'Talgar');
INSERT INTO employee VALUES ('yaslan', 'Makataeva Seifullina))', 'Uzynagash');
INSERT INTO employee VALUES ('Nursat', 'Lenina 43', 'Talgar');
INSERT INTO employee VALUES ('Adema', 'Merkur-grad', 'Almaty');
INSERT INTO employee VALUES ('Darina', 'Kutuzova 234', 'Pavlodar');
'''


current.execute(sql)

# final = current.fetchall()
# print(final)

current.close()
config.commit()
config.close()
