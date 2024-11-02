import sqlite3

connection = sqlite3.connect('convenience_store_db.db')

cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
                Id INTEGER PRIMARY KEY,
                Username TEXT NOT NULL,
                PasswordHash TEXT NOT NULL,
                Role TEXT NOT NULL CHECK(Role = 'admin' OR Role = 'employe')
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Products(
                Id INTEGER PRIMARY KEY,
                ProdName TEXT NOT NULL,
                UnitPrice REAL CHECK(UnitPrice > 0),
                QtyPerPack INTEGER CHECK(QtyPerPack > 0), -- La quantite pour chaque groupe d'un produit (un carton ou un rack de produits)
                Expiration DATETIME2(7) NOT NULL, -- La date d'expiration ou le bestbefore du produit
                ProductType TEXT NOT NULL CHECK(ProductType = 'Beverage' OR ProductType = 'Treat' OR ProductType = 'Grocery'),
                TreatType TEXT CHECK(TreatType = 'Bonbon' OR TreatType = 'Biscuit'), -- pour les produits de type treat
                Origine TEXT, -- pour les produits de type grocery (l'origine du produit)
                BeverageType TEXT CHECK(BeverageType = 'Jus' OR BeverageType = 'Soda' OR BeverageType = 'Alcool'), -- pour les produits de type Beverage 
                UserId INTEGER NOT NULL,
                FOREIGN KEY(UserId) REFERENCES Users(Id)  -- L'utilisateur qui ajoute le produit


)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS ProductsInStock(
                Id INTEGER PRIMARY KEY,
                Stock INTEGER CHECK(Stock >= 0), -- La quantite de produit disponible dans le stock
                StoreQty INTEGER CHECK(StoreQty > 0), -- La quantite envoye du stock vers le magasin
                ProductId INTEGER NOT NULL,
                FOREIGN KEY (ProductId) REFERENCES Products(Id) ON DELETE CASCADE
                )
''')