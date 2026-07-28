name = "Alice"
drink = "latte"
price = 4.50

# The f-string automatically formats the variables inside the string
receipt = f"Order for {name}: {drink} — ₦{price:.2f}"

print(receipt)

