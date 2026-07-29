prices = [100, 250, 400, 90]

def add_tax(price):
    return price * 1.10

with_tax = list(map(add_tax, prices))
print(with_tax)


# Same thing, without a lambda (to show why lambda is the natural fit here):