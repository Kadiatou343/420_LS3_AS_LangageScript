from Data_Access.DAOs.ProductDAO import ProductDAO


class GroceryDAO(ProductDAO):
    def __init__(self):
        super().__init__()

    def create_grocery(self, grocery):
        self.cursor.execute('''
           INSERT INTO Products 
           (ProdName, UnitPrice, QtyPerPack, Expiration, ProductType, Origine) 
           VALUES (?, ?, ?, ?, ?, ?)''', (grocery.get_product_name(), grocery.get_unit_price(),
                                          grocery.get_qty_per_pack(), "Grocery", grocery.get_treat_type(),))

    def update_grocery(self, grocery):
        self.cursor.execute('''UPDATE Products SET ProdName = ?, UnitPrice =? , 
        QtyPerPack=?, Expiration=?, Origine =? 
        WHERE Id = ? AND ProductType = ?''', (grocery.get_product_name(), grocery.get_unit_price(),
                                              grocery.get_qty_per_pack(), grocery.get_treat_type(),
                                              grocery.get_id(), "Grocery",))
        self.connection.commit()

    def delete_grocery(self, grocery):
        self.cursor.execute('''  DELETE FROM Products 
          WHERE Id = ? AND ProductType = ? ''', (grocery.get_id(), "Grocery",))
        self.connection.commit()