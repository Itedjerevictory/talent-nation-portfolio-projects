# Global variable (written on the public whiteboard)
menu_price = 4.50

def serve_customer(name):
    # We can read the global variable naturally
    print(f"Charging {name} ₦{menu_price:.2f} for their latte.")

serve_customer("Alice")







# Variables declared outside of any function belong to the global scope. They live from the moment they are created until the entire script finishes running, and they can be read from anywhere inside your file.