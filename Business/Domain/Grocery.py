from Business.Domain.Produits import Produit


class Grocery(Produit):
    def __init__(self,origine):
        super().__init__(origine)