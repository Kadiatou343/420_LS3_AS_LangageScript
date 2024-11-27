from Business.Domain.Beverage import Beverage
from Data_Access.DAOs.ProductDAO import ProductDAO


class BeverageDAO(ProductDAO):
    def __init__(self):
        super().__init__()


    def create_beverage(self, beverage):
        self.cursor.execute('''
        INSERT INTO Products 
        (ProdName, UnitPrice, QtyPerPack, Expiration, ProductType, BeverageType, UserId) 
        VALUES (?, ?, ?, ?, ?, ?, ?)''', (beverage.get_product_name(), beverage.get_unit_price(),
                                       beverage.get_qty_per_pack(), beverage.get_expiration(),
                                          "Beverage", beverage.get_beverage_type(), 1,))
        self.connection.commit()



    def update_beverage(self, beverage):
        self.cursor.execute('''UPDATE Products SET ProdName = ?, UnitPrice =? , 
        QtyPerPack=?, Expiration=?, BeverageType =? 
        WHERE Id = ? AND ProductType = ?''', (beverage.get_product_name(), beverage.get_unit_price(),
                                              beverage.get_qty_per_pack(), beverage.get_expiration() ,
                                              beverage.get_beverage_type(),
                                              beverage.get_id() ,"Beverage",))
        self.connection.commit()


    def delete_beverage(self, beverage):
        self.cursor.execute('''  DELETE FROM Products 
        WHERE Id = ? AND ProductType = ? ''', (beverage.get_id(), "Beverage",))
        self.connection.commit()

    def get_by_id(self, id):
        self.cursor.execute('''
        SELECT Id, ProdName, UnitPrice, QtyPerPack, Expiration, BeverageType
        FROM Products
        WHERE Id = ? ''', (id,))
        result = self.cursor.fetchone()
        bev = Beverage(result[0], result[1], result[2], result[3], result[4], result[5])
        return bev

    def get_all_beverages(self):
        self.cursor.execute('''
        SELECT Id, ProdName, UnitPrice, QtyPerPack, Expiration, BeverageType
        FROM Products
        WHERE ProductType = ? ''', ("Beverage",))
        result = self.cursor.fetchall()
        beverages = []
        for bev in result:
            bev = Beverage(bev[0], bev[1], bev[2], bev[3], bev[4], bev[5])
            beverages.append(bev)

        return beverages