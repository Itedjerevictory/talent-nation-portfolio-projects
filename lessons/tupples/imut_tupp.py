# signature_blend = ("Vanilla", "Caramel", "Hazelnut")

# # We read the recipes without modifying the parent tuple
# print(f"To make the House Blend, use: {signature_blend[0]} and {signature_blend[1]}")


signature = ("Vanilla", "Caramel")
# Try to append:
signature.append("Hazelnut")
# does not work because tuples are immutable. You cannot add, remove, or change elements in a tuple after it has been created.





# Step 3: Immutability and Safety
# Because tuples are immutable, they do not support any modification methods. Tuples do not have .append(), .pop(), .remove(), or .sort() methods. Any attempt to write to or modify a tuple will cause a crash.