class Product:
    def __init__(self, id, product_name, unit_price, qty_per_pack, expiration):
        self.__id = id
        self.__product_name = product_name
        self.__unit_price = unit_price
        self.__qty_per_pack = qty_per_pack
        self.__expiration = expiration


    #les getters
    def get_id(self):
        return self.__id

    def get_product_name(self):
        return self.__product_name

    def get_unit_price(self):
        return self.__unit_price

    def get_qty_per_pack(self):
        return self.__qty_per_pack

    def get_expiration(self):
        return self.__expiration

    def get_user(self):
        return self.__user

    #les setters
    def set_id(self, id):
        self.__id = id

    def set_product_name(self, product_name):
        self.__product_name = product_name

    def set_unit_price(self, unit_price):
        self.__unit_price = unit_price

    def set_qty_per_pack(self, qty_per_pack):
        self.__qty_per_pack = qty_per_pack

    def set_expiration(self, expiration):
        self.__expiration = expiration

    def set_user(self, user):
        self.__user = user