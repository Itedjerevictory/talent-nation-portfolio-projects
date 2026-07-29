menu_price = 4.50  # Global

def show_price():
    # Reading is completely safe and permitted
    print(f"The whiteboard price is: ₦{menu_price:.2f}")

show_price()







# Variables declared outside of any function belong to the global scope. They live from the moment they are created until the entire script finishes running, and they can be read from anywhere inside your file.