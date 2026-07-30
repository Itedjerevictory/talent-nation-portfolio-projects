from functools import reduce

prices = [15000, 800, 3500, 6200, 400]

total = reduce(lambda running_total, current_price: running_total + current_price, prices)

print(total)





# What actually happened, step by step:

# reduce() walks through the list two items at a time, carrying forward a "running result" as it goes:

# Step 1: running_total = 15000 (first item, starting point)
# Step 2: running_total = 15000 + 800   = 15800
# Step 3: running_total = 15800 + 3500  = 19300
# Step 4: running_total = 19300 + 6200  = 25500
# Step 5: running_total = 25500 + 400   = 25900   ← final answer