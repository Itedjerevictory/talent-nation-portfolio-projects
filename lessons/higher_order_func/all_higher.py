from functools import reduce

prices = [100, 250, 400, 90]

mapped   = list(map(lambda p: p * 2, prices))          # list  -> list (same size)
filtered = list(filter(lambda p: p > 150, prices))      # list  -> smaller list
reduced  = reduce(lambda a, b: a + b, prices)            # list  -> single value

print('map:   ', mapped)
print('filter:', filtered)
print('reduce:', reduced)