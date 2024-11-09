class ProductsInStock:


    def __init__(self, id, stock, storeQty, product):
      self.__id = id
      self.__stock = stock
      self.__storeQty = storeQty
      self.__product = product

    def get_id(self):
        return self.__id

    def get_stock(self):
        return self.__stock

    def get_storeQty(self):
        return self.__storeQty

    def get_product(self):
        return self.__product


    #les setters
    def set_id(self, id):
        self.__id = id

    def set_stock(self, stock):
        self.__stock = stock

    def set_storeQty(self, storeQty):
        self.__storeQty = storeQty

    def set_product(self, product):
        self.__product = product
