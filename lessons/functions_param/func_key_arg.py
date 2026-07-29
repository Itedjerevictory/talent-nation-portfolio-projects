def brew_cup(drink, size, temperature):
    print(f"Brewing a {temperature} {size} {drink}...")

# Call using explicit names. The order of these lines does not matter!
brew_cup(temperature="iced", drink="cappuccino", size="medium")



# Keyword arguments allow you to ignore positional sequence entirely by explicitly stating the parameter name and its assigned value inside the function call: parameter_name=value.
