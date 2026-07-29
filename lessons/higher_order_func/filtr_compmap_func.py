prices = [100, 250, 400, 90, 600, 45]

doubled  = list(map(lambda p: p * 2, prices))      # transforms ALL items
expensive = list(filter(lambda p: p > 200, prices))  # keeps SOME items

print("map    (all, transformed):", doubled)
print("filter (some, unchanged): ", expensive)