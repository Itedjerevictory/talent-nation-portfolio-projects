prices = [100, 250, 400, 90]

# Apply a 10% tax to EVERY price in the list
with_tax = list(map(lambda price: price * 1.10, prices))

print(with_tax)






# Before using higher-order functions, you must understand Lambda functions. They are nameless, single-line helper functions.

#     lambda price: price * 1.08
#    ↑      ↑         ↑
#  keyword  input   what to give back (no "return" needed — it's automatic)