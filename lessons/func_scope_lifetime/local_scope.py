def make_latte():
    # These are local variables (napkin notes)
    coffee_grams = 18
    milk_ounces = 8
    
    print(f"Brewing with {coffee_grams}g of coffee and {milk_ounces}oz of milk.")

make_latte()

# This will CRASH the program!
# print(coffee_grams)






# Any variable created inside a function belongs to that function's local scope. It is born when the function starts executing, lives while the function is running, and is completely destroyed (dies) the moment the function finishes.