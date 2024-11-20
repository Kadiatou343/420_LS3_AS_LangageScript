from Business.Domain.Products import Produit


class Treat(Produit):
    def __init__(self, treatType):
        super().__init__(treatType)
