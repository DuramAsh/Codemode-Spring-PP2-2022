import psycopg2

config = psycopg2.connect(
    host='localhost',
    database='postgres',
    user='postgres',
    password='Ebalokratosa.228'
)

current = config.cursor()


sql = '''
INSERT INTO works VALUES ('Aibergen', 'Tungi Kobelek', 200000);
INSERT INTO works VALUES ('Adema', 'Google', 2000000);
INSERT INTO works VALUES ('Darina', 'Orystar_club_Cumelot', 7182);
INSERT INTO works VALUES ('yaslan', 'Maqpal', 30000000);
INSERT INTO works VALUES ('Danial', 'Orystar_club_Cumelot', -1500);
'''


current.execute(sql)

# final = current.fetchall()
# print(final)

current.close()
config.commit()
config.close()
