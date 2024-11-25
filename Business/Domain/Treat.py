from Business.Domain.Product import Product


class Treat(Product):

    def __init__(self, id, product_name, unit_price, qty_per_pack, expiration, user, treat_type):
        super().__init__(id, product_name, unit_price, qty_per_pack, expiration, user)
        self.__treat_type = treat_type

    def get_treat_type(self):
        return self.__treat_type

    def set_treat_type(self, treat_type):
        self.__treat_type = treat_type