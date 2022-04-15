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

insert = 'INSERT INTO students VALUES(%s, %s);'
insert_course = 'INSERT INTO courses VALUES(%s, %s);'

make_relationship = 'INSERT INTO course_students VALUES (%s, %s, %s)'

# current.execute(insert,(1, 'Alikh'))
# current.execute(insert,(2, 'Morti'))
# current.execute(insert,(3, 'Akmira'))
# current.execute(insert,(7, 'Bauka'))

# current.execute(insert_course,(1, 'Physics'))
# current.execute(insert_course,(2, 'Calculus'))
# current.execute(insert_course,(3, 'Statistics'))
# current.execute(insert_course,(228, 'Android'))

# current.execute(make_relationship, (3, 1, 'Spring'))
# current.execute(make_relationship, (1, 2, 'Spring'))
# current.execute(make_relationship, (2, 3, 'Spring'))

# current.execute(make_relationship, (3, 3, 'Spring'))
# current.execute(make_relationship, (1, 3, 'Spring'))
# current.execute(make_relationship, (2, 2, 'Spring'))
# current.execute(make_relationship, (7, 228, 'Summer'))
current.execute(make_relationship, (7, 3, 'Fall'))

# current.execute(create_tables)



current.close()
config.commit()
config.close()