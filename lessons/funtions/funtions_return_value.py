# Definition
def calculate_price(count, cost):
    total = count * cost
    return total  # Send the calculated float back

# Call and save the returned value in a variable
cups_ordered = 3
price_per_cup = 4.50
customer_receipt = calculate_price(cups_ordered, price_per_cup)
print(f"Customer receipt: ${customer_receipt:.2f}")
