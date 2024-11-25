class User:
    def __init__(self, id, username, password_hash, role):
        self.__id = id
        self.__username = username
        self.__password_hash = password_hash
        self.__role = role

    # les getters

    def get_id(self):
        return self.__id

    def get_username(self):
        return self.__username

    def get_password_hash(self):
        return self.__password_hash

    def get_role(self):
        return self.__role

    # les setters
    def set_id(self, id):
        self.__id = id

    def set_username(self, username):
        self.__username = username

    def set_password_hash(self, password_hash):
        self.__password_hash = password_hash

    def set_role(self, role):
        self.__role = role
