# Connect to the database.
import pymysql

class database:
    def __init__(self, db):
        self.db = db
        self.conn = pymysql.connect(
            db=database_name,
            user='root',
            passwd='',
            host='localhost')
        self.c = conn.cursor()

    def add_row(args):
        c.execute("INSERT INTO " + str(self.db) + " VALUES (" + ','.join(args) + ")")

    def get_all():
        c.execute("SELECT * FROM " + str(self.db))
        result = c.fetchall()
        for row in result:
            print(row, '\n')

    def get_values(args):
        c.execute("SELECT " + str(args) + " FROM " + str(self.db))
        print([row for row in c.fetchall()])

    def get_filtered(args, filter):
        c.execute("SELECT " + str(args) + " FROM " + str(self.db) + " where " + str(filter))
        print([row for row in c.fetchall()])
        
