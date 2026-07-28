def make_custom_drink(base_drink, milk_type, sugar_packets):
    # Assemble the descriptive string step-by-step
    description = f"{base_drink} with {milk_type} milk"
    
    if sugar_packets > 0:
        description = description + f" and {sugar_packets} sugar packets"
        
    return description

# Generate distinct order strings
order1 = make_custom_drink("Latte", "almond", 2)
order2 = make_custom_drink("Cappuccino", "whole", 0)

print(order1) # "Latte with almond milk and 2 sugar packets"
print(order2) # "Cappuccino with whole milk"