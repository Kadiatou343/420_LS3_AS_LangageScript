from Data_Access.DAOs.ProductDAO import ProductDAO


class BeverageDAO(ProductDAO):
    def __init__(self):
        super().__init__()


    def create_beverage(self, beverage):
        self.cursor.execute('''
        INSERT INTO Products 
        (ProdName, UnitPrice, QtyPerPack, Expiration, ProductType, BeverageType) 
        VALUES (?, ?, ?, ?, ?, ?)''', (beverage.get_product_name(), beverage.get_unit_price(),
                                       beverage.get_qty_per_pack(), "Beverage", beverage.get_treat_type(),))



    def update_treat(self, beverage):
        self.cursor.execute('''UPDATE Products SET ProdName = ?, UnitPrice =? , 
        QtyPerPack=?, Expiration=?, BeverageType =? 
        WHERE Id = ? AND ProductType = ?''', (beverage.get_product_name(), beverage.get_unit_price(),
                                              beverage.get_qty_per_pack(), beverage.get_treat_type(),
                                              beverage.get_id() ,"Beverage",))
        self.connection.commit()


    def delete_treat(self, beverage):
        self.cursor.execute('''  DELETE FROM Products 
        WHERE Id = ? AND ProductType = ? ''', (beverage.get_id(), "beverage",))
        self.connection.commit()