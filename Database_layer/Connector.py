import psycopg2
from .settings import DB_NAME, USER


class Connector:
    def __init__(self):
        self.name = DB_NAME
        self.user = USER
        self.conn = psycopg2.connect("dbname={} user={}".format(
            self.name, self.user))
        self.cursor = self.conn.cursor()

    def execute_query(self, query, values):
        self.cursor.execute(query, values)

    def execute(self, query):
        self.cursor.execute(query)


    def all(self, query, values=None):
        if values is None:
            self.cursor.execute(query)
        else:
            self.cursor.execute(query, values)
        return self.cursor.fetchall()

    def get(self, query, values=None):
        if values is None:
            self.cursor.execute(query)
        else:
            self.cursor.execute(query, values)
        return self.cursor.fetchone()

    def close(self):
        self.conn.close()

    def commit(self):
        self.conn.commit()
