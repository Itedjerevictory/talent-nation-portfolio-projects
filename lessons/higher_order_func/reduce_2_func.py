from functools import reduce

prices = [15000, 800, 3500, 6200, 400]

highest = reduce(lambda biggest_so_far, current: current if current > biggest_so_far else biggest_so_far, prices)

print(highest)

