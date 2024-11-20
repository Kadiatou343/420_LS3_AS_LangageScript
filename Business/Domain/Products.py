class Produit:
    def __init__(self,id, produitName, unitPrice,qtyPerPack,expiration,user):
        self.__id = id
        self.__produitName = produitName
        self.__unitPrice = unitPrice
        self.__qtyPerPack = qtyPerPack
        self.__expiration = expiration
        self.__user = user


    #les getters
    def get_id(self):
        return self.__id

    def get_produitName(self):
        return self.__produitName

    def get_unitPrice(self):
        return self.__unitPrice

    def get_qtyPerPack(self):
        return self.__qtyPerPack

    def get_expiration(self):
        return self.__expiration

    def get_user(self):
        return self.__user

    #les setters
    def set_id(self, id):
        self.__id = id

    def set_produitName(self, produitName):
        self.__produitName = produitName

    def set_unitPrice(self, unitPrice):
        self.__unitPrice = unitPrice

    def set_qtyPerPack(self, qtyPerPack):
        self.__qtyPerPack = qtyPerPack

    def set_expiration(self, expiration):
        self.__expiration = expiration

    def set_user(self, user):
        self.__user = user