from models.items import *

item1 = Items("Plunger", 5.99, 3, True)
item2 = Items("Bath Plug", 2.75, 9, True)
item3 = Items("Light Bulb", 4.50, 12, True)

items = [item1, item2, item3]

def add_new_item(item):
    items.append(item)
