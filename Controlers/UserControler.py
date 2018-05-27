from Database_layer.UserModel import UserModel
special_charcters = ['!', '@', '?', '$', '%', '&', '^', '(', ')']
import hashlib
import crypt


class UserException(Exception):
    pass


class UserControler():

    def __init__(self):
        self.UserModel = UserModel()

    def user_exist(self, username):
        if self.UserModel.get_count_by_name(username)[0] == 1:
            return True
        return False

    def valid_password(self, password):
        if len(password) < 6:
            return False
        if sum(1 for c in password if c.isupper()) == 0:
            return False
        for i in special_charcters:
            if i in password:
                return True
        return False

    def hash_password(self, password, salt):
        ps = password + salt
        return hashlib.sha256(ps.encode('utf-8')).hexdigest()

    def check_password(self, password, hashed_password, salt):
        ps = self.hash_password(password, salt)
        return hashed_password == ps

    def generete_salt(self):
        return crypt.mksalt(crypt.METHOD_SHA512)

    def register_user(self, username, password):
        if type(username) is not str:
            raise TypeError('username must be string')
        if type(password) is not str:
            raise TypeError('password must be string')

        if self.user_exist(username) is True:
            raise UserException('user already is registered')
        salt = self.generete_salt()
        hashed = self.hash_password(
            password, salt)
        self.UserModel.insert_user(username, hashed, salt)

    def get_user_by_id(self, id):
        if type(id) is not int:
            raise TypeError('id must be string')

        if self.UserModel.get_count_by_id(id)[0] == 0:
            raise UserException('User dont exist')

        return self.UserModel.get_by_id(id)

    def get_user_by_name(self, name):
        if type(name) is not str:
            raise TypeError('name must be str')

        if self.UserModel.get_count_by_name(name)[0] == 0:
            raise UserException('User dont exist')

        return self.UserModel.get_user_by_name(name)

    def delete_user_by_id(self, id):
        if type(id) is not int:
            raise TypeError('id must be int')

        if self.UserModel.get_count_by_name()[0] == 0:
            raise ValueError('user dont exist')

        self.UserModel.delete_by_id(id)

    def delete_user_by_name(self, name):
        if type(name) is not str:
            raise TypeError('name must be string')

        if self.UserModel.get_count_by_name()[0] == 0:
            raise UserException('user dont exist')

        self.UserModel.delete_user_by_name(name)


    def commit(self):
        self.UserModel.commit()