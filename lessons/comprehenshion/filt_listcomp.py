
# ordered_sizes = ["small", "large", "medium", "large", "small"]
# large_only = [size for size in ordered_sizes if size == "large"]
# print(large_only)

# compare the filter version to the comprehension version

ordered_sizes = ["small", "large", "medium", "large", "small"]
via_filter = list(filter(lambda size: size == "large", ordered_sizes))
via_comprehension = [size for size in ordered_sizes if size == "large"]

print('filter version:       ', via_filter)
print('comprehension version:', via_comprehension)


# Step 2: Filtering Inside List Comprehensions
# To filter out items from your source list, you add an if statement to the very end of your comprehension. Python will evaluate the condition for each item, only keeping the ones that return True.