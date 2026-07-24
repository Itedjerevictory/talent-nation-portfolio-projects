# Example script — calculates the cost of coffee orders

# Set prices for different drinks
espresso_price = 3.50
latte_price = 4.50
cappuccino_price = 4.00

# Get the number of drinks ordered
num_espresso = 2
num_latte = 3
num_cappuccino = 1

# Calculate the total cost
total = (num_espresso * espresso_price) + \
        (num_latte * latte_price) + \
        (num_cappuccino * cappuccino_price)

# Check if total is above the minimum for a discount
discount = 0.10
if total > 20:
    total = total - (total * discount)  # Apply 10% discount
    print("Discount applied!")
else:
    print("No discount available")

# Print the final total
print(f"Total cost: ₦{total}")
print("Thank you for your order!")
