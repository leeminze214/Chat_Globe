import psycopg2
#https://hackersandslackers.com/psycopg2-postgres-python
class db_methods():
    def __init__(self,config):
        self.config = config()
        self.conn = None

    def connect(self):
        if self.conn is None:
            self.conn = psycopg2.connect(**self.config)
            print('data base succesfully connected')

    #will store all sorts of querie/sql methods 
    