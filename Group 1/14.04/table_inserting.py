import psycopg2

config = psycopg2.connect(
    host='localhost',
    database='postgres',
    user='postgres',
    password='Ebalokratosa.228'
)

current = config.cursor()


sql = '''
INSERT INTO employee
VALUES ('Danial', 'Zhatashka 70', 'Taraz');
INSERT INTO employee
VALUES ('Aibergen', 'Momyshuly 12', 'Talgar');
INSERT INTO employee
VALUES ('yaslan', 'Makataeva Seifullina))', 'Uzynagash');
INSERT INTO employee
VALUES ('Nursat', 'Lenina 43', 'Talgar');
INSERT INTO employee
VALUES ('Adema', 'Merkur-grad', 'Almaty');
INSERT INTO employee
VALUES ('Darina', 'Kutuzova 234', 'Pavlodar');


INSERT INTO company
VALUES ('Google', 'New-York');
INSERT INTO company
VALUES ('Maqpal', 'Uzynagash');
INSERT INTO company
VALUES ('Tungi Kobelek', 'Talgar');
INSERT INTO company
VALUES ('Qysqaagash', 'Uzynagash');
INSERT INTO company
VALUES ('Orystar_club_Cumelot', 'Pavlodar');

INSERT INTO works
VALUES ('yaslan', 'Tungi Kobelek', 150000);
INSERT INTO works
VALUES ('Aibergen', 'Tungi Kobelek', 200000);
INSERT INTO works
VALUES ('Adema', 'Google', 2000000);
INSERT INTO works
VALUES ('Darina', 'Orystar_club_Cumelot', 7182);
INSERT INTO works
VALUES ('yaslan', 'Maqpal', 30000000);
INSERT INTO works
VALUES ('Danial', 'Orystar_club_Cumelot', -1500);
'''


current.execute(sql)

# final = current.fetchall()
# print(final)

current.close()
config.commit()
config.close()
