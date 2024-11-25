class ProductsInStock:


    def __init__(self, id, stock, store_qty, product):
      self.__id = id
      self.__stock = stock
      self.__store_qty = store_qty
      self.__product = product

    def get_id(self):
        return self.__id

    def get_stock(self):
        return self.__stock

    def get_store_qty(self):
        return self.__store_qty

    def get_product(self):
        return self.__product


    #les setters
    def set_id(self, id):
        self.__id = id

    def set_stock(self, stock):
        self.__stock = stock

    def set_store_qty(self, store_qty):
        self.__store_qty = store_qty

    def set_product(self, product):
        self.__product = product
