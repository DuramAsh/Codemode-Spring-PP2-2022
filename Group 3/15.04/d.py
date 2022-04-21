import psycopg2
from config import data
config = psycopg2.connect(**data)

current = config.cursor()

get = '''
SELECT * FROM course_students WHERE time='Summer'; 
'''

pretty_get = '''
SELECT students.name,courses.title,time FROM students,course_students,courses 
WHERE students.id=course_students.stud_id AND courses.id=course_students.course_id AND time='Summer'; 
'''

current.execute(pretty_get)

output = current.fetchall()
print(*output, sep='\n')



current.close()
config.commit()
config.close()