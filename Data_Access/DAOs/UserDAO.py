
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
        self.connection = sqlite3.connect('../convenience_store_db.db')
        self.cursor = self.connection.cursor()

    #Les methodes de gestion de with
    # def __enter__(self):
    #     self.connection =  sqlite3.connect('convenience_store_db.db')
    #     self.cursor = self.connection.cursor()
    #     return self
    #
    # def __exit__(self, exc_type, exc_val, exc_tb):
    #     if self.cursor:
    #         self.cursor.close()
    #     if self.connection:
    #         self.connection.close()


    def get_by_id(self, user_id):
        self.cursor.execute("SELECT * FROM Users WHERE id = ?", (user_id,))
        result = self.cursor.fetchone()
        user = User(result[0], result[1], result[2], result[3])
        return user

    def get_all(self):
        self.cursor.execute("SELECT * FROM Users")
        result = self.cursor.fetchall()
        users = []
        for user in result:
            users.append(User(user[0], user[1], user[2], user[3]))

        return users

    def create_user(self, user):
        self.cursor.execute('''
        INSERT INTO Users (Username, PasswordHash, Role) 
        VALUES (?, ?, ?)
        ''', (user.get_username(), user.get_password_hash(), user.get_role(),))
        self.connection.commit()

    def update_user(self, user):
        self.cursor.execute('''
        UPDATE Users 
        SET Username = ?, PasswordHash = ?, Role = ?
        WHERE Id = ?
        ''', (user.get_username(), user.get_password_hash(), user.get_role(), user.get_id(),))
        self.connection.commit()

    def delete_user(self, user):
        self.cursor.execute("DELETE FROM Users WHERE Id = ?", (user.get_id(),))
        self.connection.commit()