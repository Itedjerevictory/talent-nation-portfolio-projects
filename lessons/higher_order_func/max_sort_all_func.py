products = [
    {'name': 'Rice bag',      'price': 15000},
    {'name': 'Bread',         'price': 800},
    {'name': 'Phone charger', 'price': 3500},
]

rule = lambda p: p['price']   # the SAME rule reused for all three

print('sorted:', [p['name'] for p in sorted(products, key=rule)])
print('min:   ', min(products, key=rule)['name'])
print('max:   ', max(products, key=rule)['name'])


# Same key=rule lambda, plugged into three different functions:

# Function	What it gives you
# sorted(list, key=...)	The whole list, rearranged by the rule
# min(list, key=...)	Just the one item ranked lowest by the rule
# max(list, key=...)	Just the one item ranked highest by the rule

# The pattern to keep for life: any time you see key=, Python is asking "how should I compare these items?" — and a lambda is almost always the fastest way to answer that question inline, without writing a separate named function just for one comparison rule.

