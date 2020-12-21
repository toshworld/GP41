import sqlite3 as sql

dbname = 'database.db'

class Sqlite:
    def create_connection(self, db_file):
        """
        create or connect to the DB
        :param db_file: str
        :return:
        """
        """ create a database connection to a SQLite database """
        self.con = None
        try:
            self.con = sql.connect(db_file,uri=True)
        except sql.Error as e:
            print(e)

    def task_select(self, select):
        """
        Executes a select statement and return results and column/field names.
        :param select:
        :return: column/field names
        """
        with self.con as conn:
            c = conn.cursor()
            c.execute(select)
            col_names = [str(name[0]).lower() for name in c.description]
            return c.fetchall(), col_names   
sq = Sqlite()
sq.create_connection(dbname)
                 

