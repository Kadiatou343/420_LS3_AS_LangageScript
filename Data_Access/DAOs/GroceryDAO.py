from Business.Domain.Grocery import Grocery
from Data_Access.DAOs.ProductDAO import ProductDAO


class GroceryDAO(ProductDAO):
    def __init__(self):
        super().__init__()

    def create_grocery(self, grocery):
        self.cursor.execute('''
           INSERT INTO Products 
           (ProdName, UnitPrice, QtyPerPack, Expiration, ProductType, Origine, UserId) 
           VALUES (?, ?, ?, ?, ?, ?, ?)''', (grocery.get_product_name(), grocery.get_unit_price(),
                                          grocery.get_qty_per_pack(), grocery.get_expiration() ,
                                             "Grocery", grocery.get_origine(),1,))
        self.connection.commit()

    def update_grocery(self, grocery):
        self.cursor.execute('''UPDATE Products SET ProdName = ?, UnitPrice =? , 
        QtyPerPack=?, Expiration=?, Origine =? 
        WHERE Id = ? AND ProductType = ?''', (grocery.get_product_name(), grocery.get_unit_price(),
                                              grocery.get_qty_per_pack(), grocery.get_expiration(),
                                              grocery.get_origine(),
                                              grocery.get_id(), "Grocery",))
        self.connection.commit()

    def delete_grocery(self, grocery):
        self.cursor.execute('''  DELETE FROM Products 
          WHERE Id = ? AND ProductType = ? ''', (grocery.get_id(), "Grocery",))
        self.connection.commit()

    def get_by_id(self, id):
        self.cursor.execute('''
        SELECT Id, ProdName, UnitPrice, QtyPerPack, Expiration, Origine 
        FROM Products 
        WHERE Id = ?''', (id,))
        result = self.cursor.fetchone()
        grocery = Grocery(result[0], result[1], result[2], result[3], result[4], result[5])
        return grocery

    def get_all_groceries(self):
        self.cursor.execute('''
        SELECT Id, ProdName, UnitPrice, QtyPerPack, Expiration, Origine
        FROM Products
        WHERE ProductType = ? ''', ("Grocery",))
        result = self.cursor.fetchall()
        groceries = []
        for grocery in result:
            grocery = Grocery(grocery[0], grocery[1], grocery[2], grocery[3], grocery[4], grocery[5])
            groceries.append(grocery)
        return groceries