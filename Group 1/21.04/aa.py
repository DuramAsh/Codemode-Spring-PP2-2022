import psycopg2

conn = psycopg2.connect(
    host='localhost', 
    database='postgres',
    port=5432,
    user='postgres',
    password='Adil2002'
)

cursor = conn.cursor()

sql = '''
create or replace function getStudentNameSurnamePhone(name varchar)
    returns setof phonebook
as
$$
begin
    return query
        select *  from phonebook
        where phonebook.username = $1;
end
$$ language plpgsql;
'''



cursor.execute(sql)

cursor.close()
conn.commit()
conn.close()

