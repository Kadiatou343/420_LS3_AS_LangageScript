from Business.Domain.Produits import Produit


class Beverage(Produit):
    def __init__(self, beverageType):
        super().__init__(beverageType)
