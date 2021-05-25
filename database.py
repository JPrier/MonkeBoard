# Connect to the database.
import pymysql

class database:
    def __init__(self, db):
        self.conn = pymysql.connect(
            db=db,
            user='root',
            passwd='',
            host='localhost')
        self.c = conn.cursor()

    def does_table_exist(table):
        c.execute("SELECT TABLES LIKE '" + str(table) + "'")
        return c.fetchone()

    def add_table(table, columns):
        c.execute("CREATE TABLE " + str(table) + str(columns))

    def add_row(args, table):
        c.execute("INSERT INTO " + str(table) + " VALUES (" + ','.join(args) + ")")

    def get_all():
        c.execute("SELECT * FROM " + str(table))
        result = c.fetchall()
        for row in result:
            print(row, '\n')

    def get_values(args):
        c.execute("SELECT " + str(args) + " FROM " + str(table))
        print([row for row in c.fetchall()])

    def get_filtered(args, filter):
        c.execute("SELECT " + str(args) + " FROM " + str(table) + " where " + str(filter))
        print([row for row in c.fetchall()])
