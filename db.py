import sqlite3
from contextlib import closing

class DB:
    @classmethod
    def exec(self, sql, args=None):
        dbname = 'database.db'
        with closing(sqlite3.connect(dbname)) as conn:
            c = conn.cursor()
            print(sql)
            if args and len(args) > 0:
                print(args)
                result = []
                for row in c.executemany(sql, args):
                    result.append(row)
            else:
                result = []
                for row in c.execute(sql):
                    result.append(row)
            conn.commit()
        return result
