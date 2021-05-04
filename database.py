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
        # # Insert some example data.
        # c.execute("INSERT INTO numbers VALUES (1, 'One!')")
        # c.execute("INSERT INTO numbers VALUES (2, 'Two!')")
        # c.execute("INSERT INTO numbers VALUES (3, 'Three!')")
        # conn.commit()
        pass

    def get_all():
        # Print the contents of the database.
        # c.execute("SELECT * FROM numbers")
        # print([(r[0], r[1]) for r in c.fetchall()])
        c.execute("SELECT * FROM numbers")
        result = c.fetchall()
        for row in result:
            print(row, '\n')
        pass

    def get_values(args):
        # c.execute("SELECT <args> FROM numbers")
        # c.fetchall
        pass

    def get_filtered(args, filter):
        # c.execute("SELECT <args> FROM numbers where <filter>")
        # c.fetchall
        pass
