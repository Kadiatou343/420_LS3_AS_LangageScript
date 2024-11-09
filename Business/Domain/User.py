class User:
    def __init__(self,id, username, passwordHash,role):
        self.__id = id
        self.__username = username
        self.__passwordHash = passwordHash
        self.__role = role


#les getters

    def get_id(self):
        return self.__id

    def get_username(self):
        return self.__username

    def get_passwordHash(self):
        return self.__passwordHash

    def get_role(self):
        return self.__role


#les setters
    def set_id(self,id):
        self.__id = id

    def set_username(self,username):
        self.__username = username

    def set_passwordHash(self,passwordHash):
        self.__passwordHash = passwordHash

    def set_role(self,role):
        self.__role = role