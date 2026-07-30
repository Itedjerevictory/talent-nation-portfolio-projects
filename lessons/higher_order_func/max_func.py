# max() — finds the single largest item, same pattern again

products = [
    {'name': 'Rice bag',      'price': 15000},
    {'name': 'Bread',         'price': 800},
    {'name': 'Phone charger', 'price': 3500},
]

priciest = max(products, key=lambda p: p['price'])
print(priciest)