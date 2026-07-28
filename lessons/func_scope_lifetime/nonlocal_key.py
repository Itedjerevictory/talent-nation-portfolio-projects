def run_coffee_cart():
    # Outer parent function's local variable
    current_order = "Espresso"
    
    def change_order(new_drink):
        nonlocal current_order  # Link to the parent function's variable
        current_order = new_drink
        print(f"Order updated to: {current_order}")

    change_order("Latte")
    print(f"Final cart order: {current_order}")

run_coffee_cart()








# When you write a nested function (a function inside a function), the inner function can read variables inside the outer parent function. To modify those parent variables, the inner function must decxlare them using the nonlocal keyword.