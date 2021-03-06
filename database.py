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

    def check_table_exists(table):
        c.execute("SELECT TABLES LIKE '" + str(table) + "'")
        return c.fetchone()

    def create_table(table, columns):
        c.execute("CREATE TABLE " + str(table) + " " + str(columns))

    def add_row(args, table):
        c.execute("INSERT INTO " + str(table) + " VALUES (" + ','.join(args) + ")")

    def get_all():
        c.execute("SELECT * FROM " + str(table))
        result = c.fetchall()
        for row in result:
            return(row, '\n')

    def get_values(args):
        c.execute("SELECT " + ','.join(args) + " FROM " + str(table))
        return([row for row in c.fetchall()])

    def get_filtered(args, filter, table):
        c.execute("SELECT " + ','.join(args) + " FROM " + str(table) + " where " + str(filter))
        return([row for row in c.fetchall()])
