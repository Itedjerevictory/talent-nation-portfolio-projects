from functools import reduce

cart = [1200, 3400, 500, 8900]

total = reduce(lambda running_total, current_item: running_total + current_item, total)
print(total)