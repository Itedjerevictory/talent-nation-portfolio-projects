# finds the single smallest item, using the same rule


products = [
    {'name': 'Rice bag',      'price': 15000},
    {'name': 'Bread',         'price': 800},
    {'name': 'Phone charger', 'price': 3500},
]

cheapest = min(products, key=lambda p: p['price'])
print(cheapest)