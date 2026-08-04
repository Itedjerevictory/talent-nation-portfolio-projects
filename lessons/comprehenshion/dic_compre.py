

menu = {"Latte": 4.50, "Espresso": 3.50, "Mocha": 5.00}

# Apply a ₦0.50 discount to every value on the menu whiteboard
discounted_menu = {drink: price - 0.50 for drink, price in menu.items()}

print(discounted_menu) # Output: {'Latte': 4.0, 'Espresso': 3.0, 'Mocha': 4.5}




# menu = {"Latte": 4.50, "Espresso": 3.50, "Mocha": 5.00}
# shouting_menu = {drink.upper(): price for drink, price in menu.items()}
# print(shouting_menu)

# Step 3: Dictionary Comprehensions
# To generate a new dictionary in-place, you use curly braces { and } and define both a key expression and a value expression separated by a colon: {key_expr: value_expr for key, value in source_dict.items()}.