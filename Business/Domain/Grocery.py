from Business.Domain.Product import Product


class Grocery(Product):
    def __init__(self, id, product_name, unit_price, qty_per_pack, expiration, origine):
        super().__init__(id, product_name, unit_price, qty_per_pack, expiration)
        self.__origine = origine


    def get_origine(self):
        return self.__origine

    def set_origine(self, origine):
        self.__origine = origine