items = ["Vanilla", "Mocha", "Mint"]

# it removes the last item from the list and returns it, so you can store it in a variable if you want to use it later. The list is now one item shorter.
last_item = items.pop()
print(f"Last item removed: {last_item}")

# it removes the item at index 0, which is "Vanilla". The list is now one item shorter.
items.remove("Vanilla")
print(f"Items after removing Vanilla: {items}")









# To take a bottle off your shelf, you can use two different tools depending on what information you have:

# .pop(index): Removes the item at a specific index and hands it back to you (returns it). If you do not provide an index, it pops the very last item.
# .remove(item_name): Searches from left to right and deletes the first item that matches item_name. It returns None.