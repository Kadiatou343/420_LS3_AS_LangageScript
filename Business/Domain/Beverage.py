from Business.Domain.Product import Product


class Beverage(Product):

    def __init__(self, id, product_name, unit_price, qty_per_pack, expiration, user, beverage_type):
        super().__init__(id, product_name, unit_price, qty_per_pack, expiration, user)
        self.__beverage_type = beverage_type

