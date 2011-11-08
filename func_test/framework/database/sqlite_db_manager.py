import sqlite3
import os

try:
    from resources.local_settings import DATABASES
except Exception as e:
    print "local_settings file is not available"

#TODO find the path, I just hard code here, need to replace in future
DB_FILE = '/Users/twer/twu/Django/PairStairs/pairstairs.db'

class DataBaseManager(object):
    def get_connections(self, database_name=DB_FILE):
        return sqlite3.connect(database_name)

    def reset_db(self):
        con = None
        cur = None
        try:
            con = self.get_connections()
            cur = con.cursor()
            cur.execute('delete from pairstairs_programmer')
            cur.execute('delete from pairstairs_pair')
            con.commit()
        finally:
            if cur:
                cur.close()
            if con:
                con.close()