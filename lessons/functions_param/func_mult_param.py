# A function with 5 distinct parameters
def record_kiosk_order(name, drink, size, milk, sugar_packets):
    print(f"Kiosk Receipt for {name}:")
    print(f"  Item: {size} {drink}")
    print(f"  Milk: {milk}")
    print(f"  Sugar: {sugar_packets} packets")

# Example usage of the function
record_kiosk_order("Alice", "Latte", "Medium", "Almond", 2)
record_kiosk_order("Bob", "Cappuccino", "Large", "Whole", 0)
record_kiosk_order("Charlie", "Espresso", "Small", "None", 1)

