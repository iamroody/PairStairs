import sqlite3
import os

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
DB_FILE = os.path.join(PROJECT_ROOT, 'pairstairs.db')


class DataBaseManager(object):
    def get_connections(self, database_name=DB_FILE):
        return sqlite3.connect(database_name)

    def reset_db(self):
        con = None
        cur = None
        try:
            con = self.get_connections()
            cur = con.cursor()
            cur.execute('delete from programmer')
            cur.execute('delete from pair')
            con.commit()
        finally:
            if cur:
                cur.close()
            if con:
                con.close()