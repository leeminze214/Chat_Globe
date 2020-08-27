'''
from config import db_conn
import psycopg2
a = db_conn()
conn = psycopg2.connect(**a)
cursor = conn.cursor()
cursor.execute('SELECT * FROM user_info;')
a =cursor.fetchone()
#you need to fetch cursor in order to get results
print(a)
'''