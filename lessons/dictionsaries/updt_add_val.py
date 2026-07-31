menu = {
    "Latte": 4.50,
    "Espresso": 3.50
}

# 1. Update an existing price (Latte increases to 5.00)
menu["Latte"] = 5.00

# 2. Add a brand-new drink to the board (Chai is added)
menu["Chai"] = 4.00

print(f"Updated menu: {menu}") # Output: {'Latte': 5.0, 'Espresso': 3.5, 'Chai': 4.0}