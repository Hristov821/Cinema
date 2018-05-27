
class user_queries():

    @classmethod
    def insert_user(cls):
        return """
    INSERT INTO Users (USERNAME,PASSWORD,SALT)
    VALUES (%s, %s, %s)
    """

    @classmethod
    def get_user_by_id(cls):
        return """
    SELECT * FROM USERS
    WHERE ID = %s
    """

    @classmethod
    def delete_user_by_id(cls):
        return """
    DELETE from Users
    WHERE ID = %s
    """

    @classmethod
    def delete_user_by_name(cls):
        return """
    DELETE FROM USERS
    WHERE USERNAME = %s
    """

    @classmethod
    def get_user_by_name(cls):
        return """
    SELECT ID,PASSWORD,SALT FROM USERS
    WHERE USERNAME = %s
    limit 1
    """

    @classmethod
    def id_exist(cls):
        return """
    SELECT COUNT(*)
    FROM USERS
    WHERE ID = %s
    """

    @classmethod
    def username_exist(cls):
        return """
    SELECT COUNT(*)
    FROM USERS
    WHERE USERNAME = %s
    """
