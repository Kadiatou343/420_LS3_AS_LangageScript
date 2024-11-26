import flask
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')
@app.route('/prod')
def product():
    return render_template('product.html')

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