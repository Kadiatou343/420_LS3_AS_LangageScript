import sqlite3

from Business.Domain.Product import Product
from Data_Access.DAOs.UserDAO import UserDAO


class ProductDAO:
    def __init__(self):
        self.connection = sqlite3.connect('../convenience_store_db.db')
        self.cursor = self.connection.cursor()
        self.userDAO = UserDAO()



    def get_all_products(self):
        self.cursor.execute("SELECT Id, ProdName, UnitPrice, QtyPerPack, Expiration, UserId FROM Products")
        results = self.cursor.fetchall()
        products = []
        for product in results:
            user = self.userDAO.get_by_id(product[5])
            products.append(Product(product[0], product[1], product[2], product[3], product[4], user))

    def get_product_by_id(self, prod_id):
        self.cursor.execute('''SELECT Id, ProdName, UnitPrice, QtyPerPack, 
        Expiration, UserId FROM Products
        WHERE Id = ?''', (prod_id,))
        result = self.cursor.fetchone()
        user = self.userDAO.get_by_id(result[5])
        return Product(result[0], result[1], result[2], result[3], result[4], user)

    def create_product(self, product):
        self.cursor.execute('''INSERT INTO Products (ProdName, UnitPrice, QtyPerPack, Expiration, UserId)
        VALUES (?, ?, ?, ?, ?)
        ''', (product.get_product_name(), product.get_unit_price(),
                          product.get_qty_per_pack(), product.get_expiration(),
                          product.get_user().get_id(),))
        self.connection.commit()


    def update_product(self, product):
        self.cursor.execute('''
        UPDATE Products SET ProdName = ?, 
        UnitPrice = ?, QtyPerPack = ?,
        Expiration = ?, UserId = ? 
        WHERE Id = ?''', (product.get_product_name(), product.get_unit_price(),
                          product.get_qty_per_pack(), product.get_expiration(),
                          product.get_user().get_id(),))
        self.connection.commit()

    def delete_product(self, product):
        self.cursor.execute("DELETE FROM Products WHERE Id = ?", (product.get_id(),))
        self.connection.commit()