def brew_cup(drink, size, temperature):
    print(f"Brewing a {temperature} {size} {drink}...")

# Call with exact positional alignment
brew_cup("Latte", "large", "hot")
brew_cup("Cappuccino", "medium", "iced")
brew_cup("Espresso", "small", "hot")

# By default, Python maps arguments to parameters based on their physical position in the function call. The first argument goes to the first parameter, the second to the second, and so on.