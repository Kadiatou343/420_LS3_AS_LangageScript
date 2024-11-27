from Business.Domain.Treat import Treat
from Data_Access.DAOs.ProductDAO import ProductDAO


class TreatDAO(ProductDAO):

    def __init__(self):
        super().__init__()

    def create_treat(self, treat):
        self.cursor.execute('''
        INSERT INTO Products 
        (ProdName, UnitPrice, QtyPerPack, Expiration, ProductType, TreatType, UserId) 
        VALUES (?, ?, ?, ?, ?, ?, ?)''', (treat.get_product_name(), treat.get_unit_price(),
                                        treat.get_qty_per_pack(), treat.get_expiration(), "Treat",
                                          treat.get_treat_type(), 1,))
        self.connection.commit()


    def update_treat(self, treat):
        self.cursor.execute('''UPDATE Products SET ProdName = ?, UnitPrice =? , 
        QtyPerPack=?, Expiration=?, TreatType =? 
        WHERE Id = ? AND ProductType = ?''', (treat.get_product_name(), treat.get_unit_price(),
                                              treat.get_qty_per_pack(), treat.get_expiration(),treat.get_treat_type(),
                                              treat.get_id(),"Treat",))
        self.connection.commit()



    def delete_treat(self, treat):
        self.cursor.execute('''  DELETE FROM Products 
        WHERE ProductType = ? AND Id = ? ''', ("Treat", treat.get_id(),))
        self.connection.commit()

    def get_by_id(self, id):
        self.cursor.execute('''
        SELECT Id, ProdName, UnitPrice, QtyPerPack, Expiration, TreatType 
        FROM Products 
        WHERE Id = ?''', (id,))
        result = self.cursor.fetchone()
        treat = Treat(result[0], result[1], result[2], result[3], result[4], result[5])
        return treat

    def get_all_treats(self):
        self.cursor.execute('''
        SELECT Id, ProdName, UnitPrice, QtyPerPack, Expiration, TreatType
        FROM Products
        WHERE ProductType = ?''',("Treat",))
        result = self.cursor.fetchall()
        treats = []
        for treat in result:
            treat = Treat(treat[0], treat[1], treat[2], treat[3], treat[4], treat[5])
            treats.append(treat)

        return treats