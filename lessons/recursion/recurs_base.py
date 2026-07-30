def clean_stack(mugs):
    if mugs <= 0:  # Check the stop switch first!
        return 0
        
    print("Cleaning...")
    clean_stack(mugs - 1)

clean_stack(3)
