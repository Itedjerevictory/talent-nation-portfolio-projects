# # The Syntax: [expression for variable in source_list]
# standard_pumps = [1, 2, 3]
# doubled_pumps = [p * 2 for p in standard_pumps]

# print(doubled_pumps) # Output: [2, 4, 6]


pumps = [1, 2, 3]
via_map = list(map(lambda p: p * 2, pumps))
via_comprehension = [p * 2 for p in pumps]

print('map version:          ', via_map)
print('comprehension version:', via_comprehension)





# A list comprehension is written inside standard square brackets [ and ]. It contains three essential parts:

# The Expression: What you want to do to each item (e.g., pumps * 2).
# The Loop Variable: The temporary placeholder name (e.g., p).
# The Iterable: The source list you are reading from (e.g., pumps).