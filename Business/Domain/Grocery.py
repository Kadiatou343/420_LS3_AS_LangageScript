from Business.Domain.Product import Product


class Grocery(Product):
    def __init__(self, id, product_name, unit_price, qty_per_pack, expiration, user, origine):
        super().__init__(id, product_name, unit_price, qty_per_pack, expiration, user)
        self.__origine = origine