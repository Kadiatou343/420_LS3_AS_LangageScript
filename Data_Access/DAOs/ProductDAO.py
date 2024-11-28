import sqlite3

from Business.Domain.Product import Product


class ProductDAO:
    def __init__(self):
        self.connection = sqlite3.connect('./Data_Access/convenience_store_db.db', check_same_thread=False)
        self.cursor = self.connection.cursor()


    def get_product_by_id(self, prod_id):
        self.cursor.execute('''SELECT Id, ProdName, UnitPrice, QtyPerPack, 
        Expiration FROM Products
        WHERE Id = ?''', (prod_id,))
        result = self.cursor.fetchone()
        return Product(result[0], result[1], result[2], result[3], result[4])
