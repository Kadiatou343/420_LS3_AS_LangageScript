import flask
from flask import Flask, render_template

from Data_Access.DAOs.BeverageDAO import BeverageDAO
from Data_Access.DAOs.GroceryDAO import GroceryDAO
from Data_Access.DAOs.TreatDAO import TreatDAO

treat_dao = TreatDAO()
groc_dao = GroceryDAO()
bev_dao = BeverageDAO()
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')
@app.route('/prod')
def product():
    treats = treat_dao.get_all_treats()
    groceries = groc_dao.get_all_groceries()
    beverages = bev_dao.get_all_beverages()
    return render_template('product.html', treats=treats, groceries=groceries, beverages=beverages)

@app.route('/stock')
def stock():
    return render_template('stock.html')

@app.route('/treat')
def add_treat():
    return render_template('addTreat.html')

@app.route('/beverage')
def add_beverage():
    return render_template('addBeverage.html')

@app.route('/grocery')
def add_grocery():
    return render_template('addGrocery.html')

if __name__ == '__main__':
    app.run(debug=True)