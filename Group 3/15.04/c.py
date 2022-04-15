import psycopg2
from config import data
config = psycopg2.connect(**data)

current = config.cursor()

create_tables = '''
CREATE TABLE students(
    id INT PRIMARY KEY,
    name varchar NOT NULL
);



CREATE TABLE courses(
    id INT PRIMARY KEY,
    title varchar NOT NULL
);

CREATE TABLE course_students(
    stud_id INT,
    FOREIGN KEY(stud_id) REFERENCES students(id),
    course_id INT,
    FOREIGN KEY (course_id) REFERENCES courses(id),
    time VARCHAR NOT NULL
);
'''

current.execute('SELECT version();')

db_version = current.fetchall()


print("Psql version:")
print(db_version)

current.close()
config.close()