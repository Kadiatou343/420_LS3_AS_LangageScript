from Data_Access.DAOs.ProductDAO import ProductDAO


class TreatDAO(ProductDAO):

    def __init__(self):
        super().__init__()

    def create_treat(self, treat):
        self.cursor.execute('''
        INSERT INTO Products 
        (ProdName, UnitPrice, QtyPerPack, Expiration, ProductType, TreatType) 
        VALUES (?, ?, ?, ?, ?, ?)''', (treat.get_product_name(), treat.get_unit_price(),
                                       treat.get_qty_per_pack(), "Treat", treat.get_treat_type(),))


    def update_treat(self, treat):
        self.cursor.execute('''UPDATE Products SET ProdName = ?, UnitPrice =? , 
        QtyPerPack=?, Expiration=?, TreatType =? 
        WHERE Id = ? AND ProductType = ?''', (treat.get_product_name(), treat.get_unit_price(),
                                              treat.get_qty_per_pack(), treat.get_treat_type(),
                                              treat.get_id() ,"Treat",))
        self.connection.commit()



    def delete_treat(self, treat):
        self.cursor.execute('''  DELETE FROM Products 
        WHERE Id = ? AND ProductType = ? ''', (treat.get_id(), "Treat",))
        self.connection.commit()