specials_tray = {"Cinnamon", "Cocoa", "Vanilla"}

# Safely check membership
if "Cinnamon" in specials_tray:
    print("Sprinkling cinnamon on the drink...")

if "Chocolate" not in specials_tray:
    print("No chocolate available.")


toppings = {"Cinnamon", "Cocoa"}
print("Cinnamon" in toppings)
print("Nutmeg" not in toppings)



# Step 2: Membership Testing (in and not in)
# Because sets have no indexes, you cannot use numbers to read items. Instead, you check if an item is present using the in or not in operators, which return a boolean True or False.