total_sales = 0.0  # Global

def record_sale(amount):
    global total_sales  # Explicitly link to the global variable
    total_sales = total_sales + amount
    print(f"Sale recorded: ₦{amount:.2f}")

record_sale(4.50)
print(f"Register total sales: ₦{total_sales:.2f}")







# To modify a global variable from inside a function, you must declare it with the global keyword at the very beginning of the function body. This tells Python: "Do not create a new local napkin note. Use the whiteboard variable on the wall."