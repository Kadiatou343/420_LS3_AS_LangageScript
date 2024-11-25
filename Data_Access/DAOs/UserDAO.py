
"""
Classe représentant la classe d'accès aux données

"""
import sqlite3

from Business.Domain.User import User


class UserDAO:
    """
    Le constructeur de la classe
    """
    def __init__(self):
        self.__connection = sqlite3.connect('convenience_store_db.db')
        self.__cursor = self.__connection.cursor()


    def get_by_id(self, user_id):
        self.__cursor.execute("SELECT * FROM Users WHERE id = ?", (user_id,))
        result = self.__cursor.fetchone()
        user = User(result[0], result[1], result[2], result[3])
        return user

    def get_all(self):
        self.__cursor.execute("SELECT * FROM Users")
        result = self.__cursor.fetchall()
        users = []
        for user in result:
            users.append(User(user[0], user[1], user[2], user[3]))

        return users

    def create_user(self, user):
        self.__cursor.execute('''
        INSERT INTO Users (Username, PasswordHash, Role) 
        VALUES (?, ?, ?)
        ''', (user.get_username(), user.get_password_hash(), user.get_role(),))
        self.__connection.commit()

    def update_user(self, user):
        self.__cursor.execute('''
        UPDATE Users 
        SET Username = ?, PasswordHash = ?, Role = ?
        WHERE Id = ?
        ''', (user.get_username(), user.get_password_hash(), user.get_role(), user.get_id(),))
        self.__connection.commit()

    def delete_user(self, user):
        self.__cursor.execute("DELETE FROM Users WHERE Id = ?", (user.get_id(),))
        self.__connection.commit()