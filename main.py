import sqlite3

import flask
from flask import Flask, render_template, request, redirect, url_for

from Business.Domain.Beverage import Beverage
from Business.Domain.Grocery import Grocery
from Business.Domain.Treat import Treat
from Business.Domain.User import User
from Data_Access.DAOs.BeverageDAO import BeverageDAO
from Data_Access.DAOs.GroceryDAO import GroceryDAO
from Data_Access.DAOs.TreatDAO import TreatDAO

treat_dao = TreatDAO()
groc_dao = GroceryDAO()
bev_dao = BeverageDAO()

user = User(1, "Kadiatou", "1234", "admin")
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


@app.route('/editBeverage/<int:id>')
def edit_beverage(id):
    bev = bev_dao.get_by_id(id)
    return render_template('addBeverage.html', bev=bev)

@app.route('/editTreat/<int:id>')
def edit_treat(id):
    treat = treat_dao.get_by_id(id)
    return render_template('addBeverage.html', treat=treat)

@app.route('/editGrocery/<int:id>')
def edit_grocery(id):
    grocery = groc_dao.get_by_id(id)
    return render_template('addBeverage.html', grocery=grocery)


if __name__ == '__main__':
    app.run(debug=True)