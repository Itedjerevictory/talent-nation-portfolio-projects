products = [
    {'name': 'Rice bag',      'price': 15000},
    {'name': 'Bread',         'price': 800},
    {'name': 'Phone charger', 'price': 3500},
]

by_price = sorted(products, key=lambda p: p['price'])

for item in by_price:
    print(item['name'], '-', item['price'])





    # sorted() — arranges a list by a rule you choose

    # Without key=, sorted() wouldn't know what to compare — dictionaries don't have a natural "smaller than" order. The lambda tells it: "when comparing two products, look at their price value."
    