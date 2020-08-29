import psycopg2
import sys

sys.path.append('secret_chat\config.py')
from config import db_params
#https://hackersandslackers.com/psycopg2-postgres-python
class db_methods():
    def __init__(self):
        self.config = db_params()
        self.conn = None

    def connect(self):
        if self.conn is None:
            self.conn = psycopg2.connect(**self.config)
            print('data base succesfully connected')

    #will store all sorts of querie/sql methods 
    