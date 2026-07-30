def wash_mugs(stack_size):
    if stack_size <= 0:  # Base case catches zero and negative safety boundaries
        print("Stack is empty!")
        return
        
    print(f"Washing mug {stack_size}")
    wash_mugs(stack_size - 1)  # Safely approaches the base case

wash_mugs(3)