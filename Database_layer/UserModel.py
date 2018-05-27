
from .Connector import Connector
from .user_queris import user_queries


class UserModel():
    def __init__(self):
        self.conn = Connector()

    def insert_user(self, username, password, salt):
        self.conn.execute_query(user_queries.insert_user(),
                                (username, password, salt))

    def get_by_id(self, id):
        return self.conn.get(user_queries.get_user_by_id(), (id,))

    def delete_by_id(self, id):
        self.conn.execute(user_queries.delete_user_by_id(), (id,))

    def get_count_by_id(self, id):
        return self.conn.get(user_queries.id_exist(), (id,))

    def get_count_by_name(self, name):
        return self.conn.get(user_queries.username_exist(), (name,))

    def delete_by_name(self, name):
        self.conn.execute(user_queries.delete_user_by_name(), (name,))

    def get_user_by_name(self, name):
        return self.conn.get(user_queries.get_user_by_name(), (name,))

    def commit(self):
        self.conn.commit()