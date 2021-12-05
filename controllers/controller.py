from app import app
from flask import render_template, request
from models.shopping_list import items, add_new_item
from models.items import Items

@app.route('/items')
def index():
    return render_template('index.html', items = items)

@app.route('/items', methods=['POST'])
def add_item():
    item_name = request.form['title']
    item_price = request.form['price']
    item_quantity = request.form['quantity']
    item_bought = request.form['bought']
    new_item = Items(item_name, item_price, item_quantity, item_bought)
    add_new_item(new_item)
    return render_template('index.html', items = items)