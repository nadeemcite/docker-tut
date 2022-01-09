import psycopg2

conn = psycopg2.connect(
    database="testdb", user='postgres', 
    password='root', host='my_db', port='5432'
)

cursor = conn.cursor()
  
sql = '''CREATE TABLE employees(emp_id int,emp_name varchar, \
salary decimal); '''
  
cursor.execute(sql)
conn.commit()