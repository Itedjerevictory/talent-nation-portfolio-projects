# Required fields are declared first, optional default fields are placed last
def process_order(name, drink, size="medium"):
    print(f"{name} wants a {size} {drink}")

# Now we can safely omit the optional size argument
process_order("Alice", "Latte") # Uses the default "medium"
process_order("Bob", "Espresso", "large") # Overrides the default


# To make some arguments optional, you can assign default fallback values directly to the parameters inside the function definition using =.

# Required parameters must always be written before default parameters.