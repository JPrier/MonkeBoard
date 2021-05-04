# Connect to the database.
import pymysql

class database:
    def __init__(self, database_name):
        self.conn = pymysql.connect(
            db=database_name,
            user='root',
            passwd='',
            host='localhost')
        self.db = conn.cursor()

    def add_row():
        # # Insert some example data.
        # c.execute("INSERT INTO numbers VALUES (1, 'One!')")
        # c.execute("INSERT INTO numbers VALUES (2, 'Two!')")
        # c.execute("INSERT INTO numbers VALUES (3, 'Three!')")
        # conn.commit()
        pass

    def get_row():
        # # Print the contents of the database.
        # c.execute("SELECT * FROM numbers")
        # print([(r[0], r[1]) for r in c.fetchall()])
        pass
