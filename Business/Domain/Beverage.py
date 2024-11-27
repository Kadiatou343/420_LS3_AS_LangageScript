from Business.Domain.Product import Product


class Beverage(Product):

    def __init__(self, id, product_name, unit_price, qty_per_pack, expiration, beverage_type, user=None):
        super().__init__(id, product_name, unit_price, qty_per_pack, expiration, user)
        self.__beverage_type = beverage_type


    def get_beverage_type(self):
        return self.__beverage_type

    def set_beverage_type(self, beverage_type):
        self.__beverage_type = beverage_type