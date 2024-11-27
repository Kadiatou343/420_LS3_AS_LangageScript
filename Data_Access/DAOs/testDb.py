from Business.Domain.Beverage import Beverage
from Business.Domain.Grocery import Grocery
from Business.Domain.Treat import Treat
from Business.Domain.User import User
from Data_Access.DAOs.BeverageDAO import BeverageDAO
from Data_Access.DAOs.GroceryDAO import GroceryDAO
from Data_Access.DAOs.TreatDAO import TreatDAO
from Data_Access.DAOs.UserDAO import UserDAO

user = User(1, "Kadiatou", "1234", "admin")

user_dao = UserDAO()

groc = Grocery(1,"Farine All purpose", 7.29, 15, 2026, "Quebec", user)

gro_dao = GroceryDAO()

