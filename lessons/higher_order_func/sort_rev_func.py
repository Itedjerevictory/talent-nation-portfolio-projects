by_price_desc = sorted(products, key=lambda p: p['price'], reverse=True)

for item in by_price_desc:
    print(item['name'], '-', item['price'])




    # just add reverse=True — the lambda rule stays exactly the same, only the direction flips.


# Sorting by something other than a number — like string length
# python
# words = ['banana', 'kiwi', 'apple', 'fig']

# by_length = sorted(words, key=lambda w: len(w))
# print(by_length)

