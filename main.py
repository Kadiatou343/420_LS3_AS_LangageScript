import sqlite3

import flask
from flask import Flask, render_template, request, redirect, url_for

from Business.Domain.Beverage import Beverage
from Business.Domain.Grocery import Grocery
from Business.Domain.Product import Product
from Business.Domain.ProductsInStock import ProductsInStock
from Business.Domain.Treat import Treat
from Business.Domain.User import User
from Data_Access.DAOs.BeverageDAO import BeverageDAO
from Data_Access.DAOs.GroceryDAO import GroceryDAO
from Data_Access.DAOs.ProductDAO import ProductDAO
from Data_Access.DAOs.ProductsInStockDAO import ProductsInStockDAO
from Data_Access.DAOs.TreatDAO import TreatDAO
from Data_Access.database import cursor

treat_dao = TreatDAO()
groc_dao = GroceryDAO()
bev_dao = BeverageDAO()
prod_dao = ProductDAO()
prod_stock_dao = ProductsInStockDAO()

user = User(1, "Kadiatou", "1234", "admin")
app = Flask(__name__)

# Redirection vers la page d'accueil
@app.route('/')
def home():
    return render_template('home.html')

# Route vers la page des produits
@app.route('/prod')
def product():
    treats = treat_dao.get_all_treats()
    groceries = groc_dao.get_all_groceries()
    beverages = bev_dao.get_all_beverages()
    return render_template('product.html', treats=treats, groceries=groceries, beverages=beverages)

# Route vers la page des produits en stock
@app.route('/stocks')
def stock():
    stocks = prod_stock_dao.get_all_stocks()
    return render_template('stock.html', stocks=stocks, prod_dao=prod_dao)


# Route vers la page d'ajout et de modification des sucreries (treat)
@app.route('/treat')
def add_treat():
    return render_template('addTreat.html')


# Route vers la page d'ajout et de modification des boissons (beverage)
@app.route('/beverage')
def add_beverage():
    return render_template('addBeverage.html')


# Route vers la page d'ajout et de modification de l'épicerie (grocery)
@app.route('/grocery')
def add_grocery():
    return render_template('addGrocery.html')


# Gestion de l'ajout des trois sortes de produits
@app.route('/addTreat', methods=['POST', 'GET'])
@app.route('/addGrocery', methods=['POST', 'GET'])
@app.route('/addBeverage', methods=['POST', 'GET'])
def add_prod():
    route = request.path

    if route == '/addTreat':
        if request.method == 'POST':
            prod_name = request.form['prodName']
            unit_price = request.form['unitPrice']
            qty_per_pack = request.form['qtyPerPack']
            exp_year = request.form['expYear']
            treat_type = request.form['treatType']

            treat = Treat(0, prod_name, unit_price, qty_per_pack, exp_year, treat_type)
            treat_dao.create_treat(treat)

            return  redirect(url_for('product'))
    elif route == '/addGrocery':
        if request.method == 'POST':
            prod_name = request.form['prodName']
            unit_price = request.form['unitPrice']
            qty_per_pack = request.form['qtyPerPack']
            exp_year = request.form['expYear']
            origine = request.form['origine']

            grocery = Grocery(0, prod_name, unit_price, qty_per_pack, exp_year, origine)
            groc_dao.create_grocery(grocery)

            return redirect(url_for('product'))
    elif route == '/addBeverage':
        if request.method == 'POST':
            prod_name = request.form['prodName']
            unit_price = request.form['unitPrice']
            qty_per_pack = request.form['qtyPerPack']
            exp_year = request.form['expYear']
            beverage_type = request.form['beverageType']

            bev = Beverage(0, prod_name, unit_price, qty_per_pack, exp_year, beverage_type)
            bev_dao.create_beverage(bev)

            return redirect(url_for('product'))
    return redirect(url_for('product'))



# Recuperation de l'id du produit à modifier et recuperation du produit en question de la base de donné
# Envoi de ce produit dans la page de modification (pour les trois sortes de produit)
@app.route('/editBeverage/<int:id>')
def edit_beverage(id):
    bev = bev_dao.get_by_id(id)
    return render_template('addBeverage.html', bev=bev)

@app.route('/editTreat/<int:id>')
def edit_treat(id):
    treat = treat_dao.get_by_id(id)
    return render_template('addTreat.html', treat=treat)

@app.route('/editGrocery/<int:id>')
def edit_grocery(id):
    grocery = groc_dao.get_by_id(id)
    return render_template('addGrocery.html', grocery=grocery)


# Gestion de la modification des trois sortes de produit
@app.route('/updateGrocery', methods=['POST', 'GET'])
@app.route('/updateTreat', methods=['POST', 'GET'])
@app.route('/updateBeverage', methods=['POST', 'GET'])
def update_pro():
    route = request.path

    if route == '/updateGrocery':
        if request.method == 'POST':
            prod_name = request.form['prodName']
            unit_price = request.form['unitPrice']
            qty_per_pack = request.form['qtyPerPack']
            exp_year = request.form['expYear']
            origine = request.form['origine']
            id = request.form['id']

            grocery = Grocery(id, prod_name, unit_price, qty_per_pack, exp_year, origine)
            groc_dao.update_grocery(grocery)

            return redirect(url_for('product'))

    elif route == '/updateTreat':
        if request.method == 'POST':
            prod_name = request.form['prodName']
            unit_price = request.form['unitPrice']
            qty_per_pack = request.form['qtyPerPack']
            exp_year = request.form['expYear']
            treat_type = request.form['treatType']
            id = request.form['id']

            treat = Treat(id, prod_name, unit_price, qty_per_pack, exp_year, treat_type)
            treat_dao.update_treat(treat)

            return redirect(url_for('product'))
    elif route == '/updateBeverage':
        if request.method == 'POST':
            prod_name = request.form['prodName']
            unit_price = request.form['unitPrice']
            qty_per_pack = request.form['qtyPerPack']
            exp_year = request.form['expYear']
            beverage_type = request.form['beverageType']
            id = request.form['id']

            bev = Beverage(id, prod_name, unit_price, qty_per_pack, exp_year, beverage_type)
            bev_dao.update_beverage(bev)

            return redirect(url_for('product'))

    return redirect(url_for('product'))

# Suppresion des trois sortes de produit
@app.route('/deleteTreat/<int:id>')
def del_treat(id):
    treat = treat_dao.get_by_id(id)
    treat_dao.delete_treat(treat)
    return redirect(url_for('product'))
@app.route('/deleteGrocery/<int:id>')
def del_grocery(id):
    grocery = groc_dao.get_by_id(id)
    groc_dao.delete_grocery(grocery)
    return redirect(url_for('product'))

@app.route('/deleteBeverage/<int:id>')
def del_beverage(id):
    beverage = bev_dao.get_by_id(id)
    bev_dao.delete_beverage(beverage)
    return redirect(url_for('product'))

@app.route('/addStock/<int:prod_id>')
def prepare_stock_for_add(prod_id):
    prod = prod_dao.get_product_by_id(prod_id)
    return render_template("addStock.html", prod=prod)

@app.route('/addStock', methods=['POST', 'GET'])
def add_stock():
    if request.method == 'POST':
        prod_name = request.form['prodName']
        stock_dispo = request.form['stock']
        store_qty = request.form['storeQty']
        prod_id = request.form['prodId']
        id = request.form['id']

        prod_stock = ProductsInStock(id, stock_dispo, store_qty, prod_id)
        prod_stock_dao.create_stock(prod_stock)

        return redirect(url_for('stock'))

    return redirect(url_for('stock'))


@app.route('/editStock/<int:id>')
def edit_stock(id):
    prod_stock = prod_stock_dao.get_by_id(id)
    prod = prod_dao.get_product_by_id(prod_stock.get_product())
    return render_template("addStock.html", stock=prod_stock, prod=prod)

@app.route('/updateStock', methods=['POST', 'GET'])
def update_stock():
    if request.method == 'POST':
        prod_name = request.form['prodName']
        stock_dispo = request.form['stock']
        store_qty = request.form['storeQty']
        prod_id = request.form['prodId']
        id = request.form['id']

        prod_stock = ProductsInStock(id, stock_dispo, store_qty, prod_id)
        prod_stock_dao.update_stock(prod_stock)
        return redirect(url_for('stock'))

    return redirect(url_for('stock'))

@app.route('/deleteStock/<int:id>')
def del_stock(id):
    prod_stock = prod_stock_dao.get_by_id(id)
    prod_stock_dao.delete_stock(prod_stock)

    return redirect(url_for('stock'))

# Demarrer l'application
if __name__ == '__main__':
    app.run(debug=True)
    treat_dao.connection.close()