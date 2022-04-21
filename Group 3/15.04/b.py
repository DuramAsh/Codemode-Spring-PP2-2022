import psycopg2
from config import data

config = psycopg2.connect(**data)

current = config.cursor()

drop_table = 'DROP TABLE retaked_students;'

create_table = '''
CREATE TABLE Retaked_students(
    name VARCHAR,
    surname VARCHAR, 
    id INT,
    subject VARCHAR
);
'''

pro_table = '''
CREATE TABLE Retaked_students(
    name VARCHAR,
    surname VARCHAR,
    id INT,
    subject VARCHAR
);

DROP TABLE retaked_students;

CREATE TABLE Retaked_students(
    name            VARCHAR NOT NULL,
    surname         VARCHAR NOT NULL,
    id INT          NOT NULL UNIQUE     CHECK(id > 0),
    subject         VARCHAR NOT NULL
);

-- NOT NULL
-- CHECK(condition)
-- UNIQUE

INSERT INTO retaked_students VALUES ('Dias', 'Tulegaleiv', 7, 'Calculus II');
INSERT INTO retaked_students VALUES ('Bauka', 'Balgaziev', 77, 'WebDEV');
'''


# current.execute(drop_table)
current.execute(create_table)

current.close()
config.commit()
config.close()