import sqlite3

from Business.Domain.ProductsInStock import ProductsInStock


class ProductsInStockDAO:
    def __init__(self):
        self.connection = None
        self.cursor = None


    def connect(self):
        self.connection = sqlite3.connect('./Data_Access/convenience_store_db.db', check_same_thread=False)
        self.cursor = self.connection.cursor()

    def get_by_id(self, id):
        self.connect()
        self.cursor.execute('SELECT * FROM ProductsInStock WHERE id = ?', (id,))
        result = self.cursor.fetchone()
        stock_prod = ProductsInStock(result[0], result[1], result[2], result[3])
        self.connection.close()
        return stock_prod

    def get_all_stocks(self):
        self.connect()
        self.cursor.execute('SELECT * FROM ProductsInStock')
        result = self.cursor.fetchall()
        stocks = []
        for stock in result:
            stock = ProductsInStock(stock[0], stock[1], stock[2], stock[3])
            stocks.append(stock)
        self.connection.close()
        return stocks

    def create_stock(self, stock):
        self.connect()
        self.cursor.execute('''
        INSERT INTO ProductsInStock (Stock, StoreQty, ProductId) 
        VALUES (?, ?, ?)''', (stock.get_stock(), stock.get_store_qty(), stock.get_product(),))
        self.connection.commit()
        self.connection.close()

    def update_stock(self, stock):
        self.connect()
        self.cursor.execute('''
        UPDATE ProductsInStock SET Stock = ?, StoreQty = ?, ProductId = ? 
        WHERE Id  = ? ''', (stock.get_stock(), stock.get_store_qty(),
                            stock.get_product(), stock.get_id(),))
        self.connection.commit()
        self.connection.close()

    def delete_stock(self, stock):
        self.connect()
        self.cursor.execute('''
        DELETE FROM ProductsInStock 
        WHERE Id = ?''', (stock.get_id(),))
        self.connection.commit()
        self.connection.close()
