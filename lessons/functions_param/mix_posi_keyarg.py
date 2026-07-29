def brew_custom_cup(drink, size, temperature, milk="whole", sugar=0):
    print(f"Making a {temperature} {size} {drink} with {milk} milk.")

# Correct: Positional arguments first, then keywords to override defaults
brew_custom_cup("Latte", "large", "hot", milk="almond", sugar=1)


